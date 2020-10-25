from django import forms

class signupForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    dob = forms.DateField(label="Date of Birth", required=True)
    phone_num = forms.CharField(label="Phone number", required=True)
    address = forms.CharField(label="Address", max_length=200)