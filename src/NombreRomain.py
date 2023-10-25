

class ArabeToRomain():
    def NbrRomain(nombre):
        if nombre == 1:
            return 'I'
        elif nombre == 2:
            return 'II'
        elif nombre == 3:
            return 'III'
        elif nombre==4:
            return 'IV'
        else:
            return 'IV'

    def NombreRomain(number):
        nombre_romain = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        resultat = ''
        for chiffre, symbole in sorted(nombre_romain.items(), reverse=True):
            while number >= chiffre:
                resultat += symbole
                number -= chiffre
        return resultat

    def NbrRomain(num):
        liste1 = ['I', 'IV', 'V']
        liste2 = [1, 4, 5]
        resultat = ''
        for i in range(len(liste2) - 1, -1, -1):
            while num >= liste2[i]:
                resultat += liste1[i]
                num -= liste2[i]
        return resultat






print(ArabeToRomain.NbrRomain(49))
