from django.urls import path
from .views import LibroListView, LibroDetailView, LibroCreateView, LibroUpdateView, LibroDeleteView, UsuarioListView, \
    UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, PrestamoListView, PrestamoDetailView, \
    PrestamoCreateView, PrestamoUpdateView, PrestamoDeleteView, BibliotecaListView, BibliotecaDetailView, \
    BibliotecaCreateView, BibliotecaUpdateView, BibliotecaDeleteView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
]
