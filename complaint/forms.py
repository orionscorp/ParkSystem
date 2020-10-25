from django import forms

class complaintMessageForm(forms.Form):
    member_id = forms.IntegerField(label="Member ID", required=False)
    #Make it so that even non member can input complaint
    name = forms.CharField(label="Name", max_length=100, required=False)
    phone_num = forms.CharField(label="Phone number", required=True)
    #Both should be filled automatically if member
    #(Or make it separate forms for member and non member in front end)
    #If possible make it with session
    vehicle_number = forms.CharField(label="Vehicle number", required=True)
    complaint_message = forms.CharField(label="Complaint", required=True, widget=forms.Textarea(attrs={"style": "resize:none"}))