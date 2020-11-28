from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogo.models import Juego


class SimpelTest(TestCase):


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('juegos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'juegos/juego_list.html')
