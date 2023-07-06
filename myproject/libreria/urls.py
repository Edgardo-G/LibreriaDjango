from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_libros, name='crear'),
    path('libros/editar/<int:id>', views.editar_libros, name='editar'),
    path('libros/eliminar/<int:id>', views.eliminar_libros, name='eliminar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)