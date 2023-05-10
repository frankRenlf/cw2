from app01 import models
from app01.utils.BootstrapModelForm import BootstrapForm, BootstrapModelForm
from django.core.exceptions import ValidationError
from django import forms


class UploadForm(BootstrapForm):
    exclude_fields = ['img']
    name = forms.CharField(max_length=32)
    age = forms.IntegerField()
    img = forms.FileField()
