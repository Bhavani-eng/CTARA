from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Crop

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

from django import forms
#contract generation form
class ContractForm(forms.Form):
    farmer_name = forms.CharField(label="Farmer Name", max_length=100)
    buyer_name = forms.CharField(label="Buyer Name", max_length=100)
    harvest_date = forms.DateField(label="Expected Harvest Date", widget=forms.DateInput(attrs={'type': 'date'}))
    agreed_amount = forms.DecimalField(label="Agreed Amount (INR)", max_digits=10, decimal_places=2)

#crop listing form
class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'quantity', 'expected_price']