from django.forms import ModelForm
from .models import Persons


class PersonForm(ModelForm):
    class Meta:
        model = Persons
        fields = ('name', 'address', 'phone')
