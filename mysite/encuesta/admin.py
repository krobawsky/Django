from django.contrib import admin
from .models import Pregunta
from .models import Opcion
# Register your models here.

admin.site.register(Pregunta)
admin.site.register(Opcion)