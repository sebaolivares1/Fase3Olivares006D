from django.test import TestCase
from catalogo.forms import JuegoForm
from catalogo.models import Juego
from django.core.files.uploadedfile import SimpleUploadedFile

class JuegoFormsTest(TestCase):
    def test_valid_form(self):
        j = Juego.objects.create(title='test1', desarrollador='test', genero='test2')
        data = {'title': j.title, 'desarrollador': j.desarrollador, 'genero':j.genero}
        form = JuegoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        j = Juego.objects.create(title='', desarrollador='test', genero='test2')
        data = {'title': j.title, 'desarrollador': j.desarrollador, 'genero':j.genero}
        form = JuegoForm(data=data)
        self.assertFalse(form.is_valid())
