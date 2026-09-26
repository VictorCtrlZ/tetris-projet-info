from django.db import models

class Trait(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()