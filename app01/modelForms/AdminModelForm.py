from app01.utils.BootstrapModelForm import BootstrapModelForm
from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from app01.utils.encrypy import md5


class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["name", "password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("password not same")
        return confirm

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class AdminResetModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("password not same")
        return confirm

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        if self.instance.password == md5(pwd):
            raise ValidationError("same with former password")
        return md5(pwd)
