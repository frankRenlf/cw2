from app01 import models
from app01.utils.BootstrapModelForm import BootstrapModelForm
from django.core.exceptions import ValidationError


class PrettyModelForm(BootstrapModelForm):
    class Meta:
        model = models.PrettyNumber
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        mobile_txt = self.cleaned_data["mobile"]
        pid = self.instance.pk
        if models.PrettyNumber.objects.filter(mobile=mobile_txt).exclude(id=pid).exists():
            raise ValidationError("Number already exists")
        if len(mobile_txt) != 11:
            raise ValidationError("Length must be 11")
        return mobile_txt
