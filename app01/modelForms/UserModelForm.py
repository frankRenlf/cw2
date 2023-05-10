from app01 import models
from app01.utils.BootstrapModelForm import BootstrapModelForm
from django.core.exceptions import ValidationError


class UserModelForm(BootstrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "gender", "salary", "create_time", "depart"]
