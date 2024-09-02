from django import forms
from .models import Maquina

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'

class MaquinaUpdate(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'