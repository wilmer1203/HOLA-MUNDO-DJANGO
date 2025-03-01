from django.shortcuts import render
from django.views.generic import TemplateView


# vista  en funcion 
def hola_mundo(request):  # request es un objeto que contiene toda la informacion de la peticion del usuario
    return render(request, 'hola_mundo.html')  # render es una funcion que renderiza un template


#vistas  en clases

class chao_mundo(TemplateView):
    template_name = 'chao.html'  # le decimos a django que renderize el template hola_mundo.html

