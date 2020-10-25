from django import forms

class signupForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField()
    dob = forms.DateField(label="Date of Birth", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_num = forms.CharField(label="Phone number", required=True)
    address = forms.CharField(label="Address", max_length=200, widget=forms.Textarea(attrs={"style": "resize:none"}))