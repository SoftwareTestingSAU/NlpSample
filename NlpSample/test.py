import unittest
import numpy as np
from NlpSample.models import Metin

class MetinTest(unittest.TestCase):
    def test_fiiller_getir(self):
        veri = {
            'icerik' : 'He is playying basketball.'
        }
        metin = Metin(data=veri)
        self.assertListEqual(metin.fiiller_getir(), ['is', 'playying'])

    def test_isimler_getir(self):
        veri = {
            'icerik' : 'Jack and Mike are walking.'
        }
        metin = Metin(data=veri)
        self.assertListEqual(metin.isimler_getir(), ['Jack', 'Mike'])
