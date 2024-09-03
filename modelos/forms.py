from django import forms
from .models import Modelos

class ModelosForm(forms.ModelForm):
    class Meta:
        model = Modelos
        fields = "__all__"

class UpdateModeloForm(forms.ModelForm):
    class Meta:
        model = Modelos
        fields = "__all__"