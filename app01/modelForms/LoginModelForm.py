from app01.utils.BootstrapModelForm import BootstrapModelForm
from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from app01.utils.encrypy import md5


class LoginModelForm(BootstrapModelForm):
    code = forms.CharField(
        label="code",
        widget=forms.TextInput,
        required=True
    )

    class Meta:
        model = models.Admin
        fields = ["name", "password"]
        widgets = {
            "name": forms.TextInput,
            "password": forms.PasswordInput,
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        if self.instance.password != md5(pwd):
            raise ValidationError("wrong input")
        return md5(pwd)

    # def clean_code(self):
