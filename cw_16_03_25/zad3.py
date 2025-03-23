class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."


os1 = Osoba("Jan", "Kowalski", 30)
print(os1.przedstaw_sie())


class Pracownik(Osoba):

    def __init__(self, stanowisko, pensja, imie, nazwisko, wiek):
        self.stanowisko = stanowisko
        self.pensja = pensja

        super().__init__(imie, nazwisko, wiek)

    def info_o_pracy(self):
        return f"Pracuje jako {self.stanowisko}, zarabiam {self.pensja} zl."

class Manager (Pracownik):

    def __init__(self, lista_pracownikow, imie, nazwisko, wiek, stanowisko, pensja):
        self.lista_pracownikow = lista_pracownikow
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)

    def przedstaw_sie(self):
        return len(self.lista_pracownikow)

    def dodaj_do_zespolu(self, pracownik):
        self.lista_pracownikow.append(pracownik)

managerObj = Manager([], "Jan", "Kowalski", 30, "Manager", 3000)
managerObj.dodaj_do_zespolu(Pracownik("Kierowca", 2000, "Adam", "Nowak", 40))
managerObj.dodaj_do_zespolu(Pracownik("Kierowca", 3000, "Adam", "Nowak", 40))
managerObj.dodaj_do_zespolu(Pracownik("Kierowca", 4000, "Adam", "Nowak", 40))
print("liczba pracownikow:", managerObj.przedstaw_sie())

for pracownik in managerObj.lista_pracownikow:
    print(pracownik.przedstaw_sie(), pracownik.info_o_pracy())
