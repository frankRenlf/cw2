from app01 import models
from app01.utils.BootstrapModelForm import BootstrapModelForm
from django.core.exceptions import ValidationError


class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["number"]
