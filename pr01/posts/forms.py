from django.forms import ModelForm, TextInput
from .models import Galaxy, System, Object

class GalaxiesForm(ModelForm):
    class Meta:
        model = Galaxy
        fields = ['galaxy_name', 'radius', 'age']

        widgets = {
            "galaxy_name": TextInput(attrs={'placeholder':'Galaxy name'}),
            "radius": TextInput(attrs={'placeholder':'Radius'}),
            "age": TextInput(attrs={'placeholder':'Age'})
        }

class SystemsForm(ModelForm):
    class Meta:
        model = System
        fields = ['system_name', 'radius', 'age']

        widgets = {
            "system_name": TextInput(attrs={'placeholder':'System name'}),
            "radius": TextInput(attrs={'placeholder':'Radius'}),
            "age": TextInput(attrs={'placeholder':'Age'})
        }

class ObjectsForm(ModelForm):
    class Meta:
        model = Object
        fields = ['id','object_name', 'mass', 'radius','system_name', 'galaxy_name']

        widgets = {
            "id": TextInput(attrs={'placeholder':'id'}),
            "object_name": TextInput(attrs={'placeholder':'Object name'}),
            "mass": TextInput(attrs={'placeholder':'Mass'}),
            "Radius": TextInput(attrs={'placeholder':'Radius'}),
        }

