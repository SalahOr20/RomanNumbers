from src.NombreRomain import ArabeToRomain

import unittest
class TestNombreRomain(unittest.TestCase):
    def Hello_WOrld(self):
        pass

    def testnombre(self):

        #etant donnée chiffre 1
        nombre=1
        #etant donnée nombre romain I
        romain=ArabeToRomain.NbrRomain(nombre)
        #Test 1
        self.assertEqual('I',romain)
















