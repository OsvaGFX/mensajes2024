from django.db import models

# Create your models here.
class Publicacion(models.Model):
  texto = models.TextField()

  def __str__(self) -> str:
    return self.texto[:50]