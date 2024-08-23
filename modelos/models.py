from django.db import models


class Modelos(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    modelo = models.CharField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.modelo)