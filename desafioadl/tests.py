from django.test import TestCase

from .service import *
from .tests_data import base_data

class ServiceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        base_data(cls)
  
    def test_show(self):
        imprimir_en_pantalla()