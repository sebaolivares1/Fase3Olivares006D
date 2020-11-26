from django.db import models
from django.urls import reverse  
import uuid  

# Create your models here.
class Juego(models.Model):
    title = models.CharField(max_length=200)
    desarrollador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('juego-detail', args=[str(self.id)])

    

class JuegoInstance(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    juego= models.ForeignKey('Juego',on_delete=models.SET_NULL, null=True)
    fecha_lan= models.DateField(null=True,blank=True)


    def __str__(self):
		    return f'{self.id} ({self.juego.title})'

    def get_absolute_url(self):
         return reverse('juegoinstance-detail', args=[str(self.id)])
