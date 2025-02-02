from django.shortcuts import render     #clase 13
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.utils import translation

#Vistas generales de la aplicación

def home_view(request):
    return render(request, "general/home.html")  


# def contacto_view(request):
#     if request.POST:
#         nombre = request.POST["nombre"]
#         email = request.POST["email"]
#         comentario = request.POST["comentario"]
#         print(f'se ha enviado un correo a {nombre} del email {email} con el texto {comentario}')
    
#     return render(request,"general/contacto.html")


# def search_view(request):
#     if request.GET:
#         busqueda = request.GET['searching']

#         autores = Autor.objects.filter(nombre__icontains=busqueda)
#         editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
#         libros = Libro.objects.filter(titulo__icontains=busqueda)
        
#         context = {
#             'autores': autores,
#             'editoriales': editoriales,
#             'libros': libros
#         }
#         return render(request, "general/search.html", context)

#     return render(request, "general/search.html")

def search_view(request):
    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data["searching"]

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)

        context = {
            'autores': autores,
            'editoriales': editoriales,
            'libros': libros,
            'formulario': formulario
        }

        return render(request, "general/search.html", context)

    else:
        formulario = SearchForm()

    context = { 
        "formulario": formulario
    }

    return render(request, "general/search.html", context)

    # if request.GET:
    #     busqueda = request.GET['searching']

    #     autores = Autor.objects.filter(nombre__icontains=busqueda)
    #     editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
    #     libros = Libro.objects.filter(titulo__icontains=busqueda)
        
    #     context = {
    #         'autores': autores,
    #         'editoriales': editoriales,
    #         'libros': libros
    #     }
    #     return render(request, "general/search.html", context)

def contacto_view(request):
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            mensaje =_('se ha enviado un correo a {nombre} del email {email} con el texto {comentario}')
            print(mensaje)

            context = {
                'formulario': formulario,
            }

            messages.info(request, _("El correo se ha enviado correctamente"))

            return render(request, "general/contacto.html", context)
        
        else:
            context = {
                "formulario": formulario
            }
            return render(request, "general/contacto.html", context)

    formulario = ContactForm()
    context = {
            "formulario": formulario
        }
    return render(request, "general/contacto.html", context)

class SetLanguageView(View):
    def post(self, request, *args, ** kwargs):
        # Obtenemos el idioma seleccionado del formulario
        language = request.POST.get('language', None)

        # Si se seleccionó un idioma, lo activamos
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language

        # Redirigimos a la página desde donde se hizo la petición
        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)