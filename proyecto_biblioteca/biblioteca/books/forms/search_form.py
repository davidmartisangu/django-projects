from django import forms
from django.utils.translation import gettext as _

class SearchForm(forms.Form):
    searching = forms.CharField(
        label=_("Introduce las palabras claves para la busqueda"),
        max_length=100
    )