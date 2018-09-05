from django.db import models

class Notify(models.Model):
    cor = models.CharField(max_length = 255)
    modelo = models.CharField(max_length = 255)
    placa = models.CharField(max_length = 7)
    local = models.CharField(max_length = 255)
    #image = forms.ImageField()
    descrição = models.CharField(max_length = 255)
    photo = models.FileField(upload_to='static', null=True, blank=True)
