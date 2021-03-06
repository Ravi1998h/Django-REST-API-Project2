from django import forms
from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email', 'date'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'date': forms.SelectDateWidget(attrs={ 'class': 'form-control' }),

      }