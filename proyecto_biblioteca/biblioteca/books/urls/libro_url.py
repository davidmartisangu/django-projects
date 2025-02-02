from django.urls import path

from books.views import (
    LibroListView,
    LibroDetailView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
)

app_name = "libro"

urlpatterns = [
    path("list/", LibroListView.as_view(), name="list"),
    path("detail/<pk>/", LibroDetailView.as_view(), name="detail"),
    path("create/", LibroCreateView.as_view(), name="create"),
    path("update/<pk>/", LibroUpdateView.as_view(), name="update"),
    path("delete/<pk>/", LibroDeleteView.as_view(), name="delete"),
]