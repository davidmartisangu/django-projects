from books.models import Libro
from django.http import Http404
from django.core.exceptions import PermissionDenied

def user_can_delete_libro(function):
    def wrap(request, *args, **kwargs):
        try:
            libro=Libro.objects.get(pk=kwargs["pk"])
        except Libro.DoesNotExist:
            raise Http404
        
        if request.user == libro.created_by:
            return function(request, *args, **kwargs)
        
        raise PermissionDenied
    
    return wrap