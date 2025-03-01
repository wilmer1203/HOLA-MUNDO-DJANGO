#urls de mi aplicacion 1

from django.urls import path
from app1.views import hola_mundo, chao_mundo # importamos la vista hola_mundo de app1.views

urlpatterns = [   # urlpatterns es una lista de rutas que se pueden visitar en la aplicacion
    path('', hola_mundo),  # la vista hola_mundo se ejecutara cuando el usuario visite la url /hola-mundo/
    path('chao_mundo/', chao_mundo.as_view()),  # la vista chao_mundo se ejecutara cuando el usuario visite la url /chao-mundo/
]   

