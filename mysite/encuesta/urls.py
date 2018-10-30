from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path('', views.index, name='index'),
    # ex: localhost:8080/polls/5/
    path('<int:pregunta_id>/', views.detalle, name='detail'),
    # ex: localhost:8080/polls/5/results/
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
    # ex: localhost:8080/polls/5/vote/
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),

    # ex: localhost:8080/sumar/1/2/
    path('sumar/<int:val1>/<int:val2>', views.sumar, name='suma'),
    # ex: localhost:8080/restar/1/2/
    path('restar/<int:val1>/<int:val2>', views.restar, name='resta'),
    # ex: localhost:8080/multiplicar/1/2/
    path('multiplicar/<int:val1>/<int:val2>', views.multiplicar, name='mul'),
    # ex: localhost:8080/dividir/1/2/
    path('dividir/<int:val1>/<int:val2>', views.dividir, name='div'),

    # ex: localhost:8080/polls/demo/v1/v2
    path('demo/<str:v1>/<str:v2>', views.demo, name='demo'),

]
