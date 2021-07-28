from myapp.models import Employee
from myapp.API.serializers import empserializer
from rest_framework.viewsets import ModelViewSet


class api1(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=empserializer
