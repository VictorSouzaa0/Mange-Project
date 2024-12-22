from django.db import models

class Professor(models.Model):
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    cargaHoraria = models.DecimalField(max_digits=10, decimal_places=2)
    horarioAula = models.DecimalField(max_digits=10, decimal_places=2)
