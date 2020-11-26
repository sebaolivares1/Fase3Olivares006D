from django.test import TestCase
from catalogo.models import Juego

class JuegoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Juego.objects.create(genero='Piratas')
    
    def test_juego_genero(self):
        juego1=Juego.objects.get(id=1)
        field_label = juego1._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
