from NombreRomain import NombreRomain as nr, ArabeToRomain, NombreRomain

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
        #test 2
        #etant donne chiffre 2
        nombre=2
        #etant donne nombre romain II
        romain=ArabeToRomain.NbrRomain(nombre)
        #Test 2
        self.assertEqual(romain,'II')
        #etant donne nombre 3
        nombre=3
        #etant donne nombre romain 'III
        romain = ArabeToRomain.NbrRomain(nombre)
        #test 3
        self.assertEqual(romain,'III')
        # etant donne nombre 4
        nombre = 4
        # etant donne nombre romain 'Iv'
        romain = ArabeToRomain.NbrRomain(nombre)
        # test 3
        self.assertEqual(romain, 'IV')












