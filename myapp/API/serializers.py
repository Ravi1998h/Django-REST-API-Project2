from rest_framework import serializers
from myapp.models import Employee



class empserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
