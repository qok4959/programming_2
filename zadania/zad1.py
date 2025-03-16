import json


class AplikacjaMobilna:

    liczba_pobran=0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self):
        self.liczba_pobran += 1

    def ile_pobran(self):
        return self.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
            return cls(**dane)



obj1 = AplikacjaMobilna('Aplikacja', '1.0')
obj1.nowe_pobranie()
obj1.nowe_pobranie()
obj1.nowe_pobranie()
print("Pobrania dla obj1:", obj1.ile_pobran())

obj2 = AplikacjaMobilna.z_json('obj1.json')
obj2.nowe_pobranie()
obj2.nowe_pobranie()
print("Pobrania dla obj2:", obj2.ile_pobran())


