from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/bdd/
    path('', views.index, name='index'),
    path('lista', views.lista, name='lista'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
    path('nuevo/<slug:nom>/<int:num>/<slug:dirc>', views.nuevo, name='nuevo'),
]
