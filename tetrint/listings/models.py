from django.db import models

#Modèle de Django par défault, stock une chaîne de caractères de longueur <= 100.
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
