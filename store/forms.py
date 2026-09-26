from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "phone", "email", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Your First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Your Last Name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
            "message": forms.Textarea(attrs={"placeholder": "Write Your Message", "rows": 6}),
        }
