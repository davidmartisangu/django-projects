from django.shortcuts import render     #clase 13
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators.libro_decorator import user_can_delete_libro

class LibroListView(ListView):
    model = Libro
    template_name = "libros/LibroList.html"
    context_object_name = "libros"


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/LibroDetail.html"
    context_object_name = "libro"


@method_decorator(login_required,name="dispatch")
class LibroCreateView(CreateView):
    model = Libro
    template_name = "libros/LibroCreate.html"
    success_url = reverse_lazy("libro:list")
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required,name="dispatch")
class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libros/LibroUpdate.html"
    success_url = reverse_lazy("libro:list")    
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
    ]


@method_decorator(user_can_delete_libro,name="dispatch")
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/LibroDelete.html"
    success_url = reverse_lazy("libro:list")




# def libros_view(request):
#     return render(request, "libros/libros.html")