from rest_framework import serializers
from app01.models import Department


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
