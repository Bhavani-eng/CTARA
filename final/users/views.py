from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from .forms import ContractForm  
from .forms import CropForm
from .models import Crop


# Homepage View
def homepage(request):
    return render(request, 'users/homepage.html')  
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User Type:", user.user_type)  
            login(request, user)

            # Redirect based on user type
            if user.user_type == "farmer":
                return redirect("farmer_dashboard")
            elif user.user_type == "buyer":
                return redirect("buyer_dashboard")

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/signup.html', {'form': form})


#login page
def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # logic for proper redirection
            if user.user_type == "farmer":
                return redirect("farmer_dashboard") 
            elif user.user_type == "buyer":
                return redirect("buyer_dashboard")  
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

#dashboard requests
def farmer_dashboard(request):
    return render(request, "farmer_dashboard.html")  

def buyer_dashboard(request):
    return render(request, "buyer_dashboard.html")

#contract generation request
@login_required
def generate_contract(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            farmer_name = form.cleaned_data['farmer_name']
            buyer_name = form.cleaned_data['buyer_name']
            harvest_date = form.cleaned_data['harvest_date']
            agreed_amount = form.cleaned_data['agreed_amount']
            
            # Creation of PDF
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, "Contract Agreement")
            p.drawString(100, 700, f"Farmer: {farmer_name}")
            p.drawString(100, 675, f"Buyer: {buyer_name}")
            p.drawString(100, 650, f"Expected Harvest Date: {harvest_date}")
            p.drawString(100, 625, f"Agreed Amount: {agreed_amount} INR")
            p.showPage()
            p.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="contract.pdf")
    else:
        form = ContractForm()
    
    return render(request, "users/generate_contract.html", {"form": form})

#crop listing request
@login_required
def list_crops(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farmer = request.user
            crop.save()
            return redirect('dashboard')
    else:
        form = CropForm()

    return render(request, "users/list_crops.html", {"form": form})