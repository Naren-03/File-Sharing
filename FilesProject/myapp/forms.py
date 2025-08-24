from django import forms
from .models import UploadFile

# class CustomeAuthForm(AuthenticationForm):

class FileUploadForm(forms.ModelForm):
    # files = forms.forms.FileField(max_length=10)
    model = UploadFile
    fields = ['file']
