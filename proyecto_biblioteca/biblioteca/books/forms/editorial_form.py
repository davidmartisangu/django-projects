from django import forms
from django.forms import ModelForm
from books.models import Editorial
from django.utils.translation import gettext as _
    
class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=300, required=False)
    ciudad = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    YEARS_CHOICES = [x for x in range(1960, 2024)]
    fecha_fundacion = forms.DateField(widget=forms.SelectDateWidget(years=YEARS_CHOICES))

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe de tener al menos 5 caracteres"))
        return nombre
    
class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = [
            "nombre",
            "codigo_postal",
            "direccion",
            "email",
            "fecha_fundacion"
        ]