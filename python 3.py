# OBJEKTINIS PROGRAMAVIMAS

# class Automobilis:
#     def __init__(self, marke,modelis, metai, variklio_turis, kuro_tipas): #- konstruktorius, naudojamas pradinei objekto busenai nustatyti
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.variklio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 0
#     def automobilio_pavadinimas(self):
#         return f"Automobilio marke: {self.marke}\n Automobilio modelis: {self.modelis}\n Automobilio pagaminimo metai: {self.metai}\n Variklio turis: {self.variklio_turis}\n Kuro tipas: {self.kuro_tipas}\n"
#
#     def vaziuoti(self,km):
#         self.rida += km
#         return f"Vaziuojama {km}km. Bendra rida {self.rida} km"
#
# auto1 = Automobilis("Audi", "A8", 2021, 3.0, "Benzinas")
# auto2 = Automobilis("Subaru", "Outback", 2015, 2.5, "Dyzelinas")
# print(auto1.automobilio_pavadinimas())
# print(auto1.vaziuoti(150))
# print()
# print(auto2.automobilio_pavadinimas())
# print(auto2.vaziuoti(400))

# class Gyvunas(object):
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.svoris = svoris
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_pavadinimas(self):
#         return f" Gyvuno rusis: {self.rusis}\n Gyvuno svoris: {self.svoris}\n Gyvuno amzius: {self.amzius}\n Gyvuno vardas: {self.vardas}\n"
#     def medzioti(self):
#         return f"{self.vardas} eina medzioti"
#     def prisistatymas(self):
#         return f"As esu pilkas {self.rusis} vardu {self.vardas}"
#   
# gyvunas1 = Gyvunas ("vilkas", "50", "7", "Balu")
# print(gyvunas1.gyvuno_pavadinimas())
# print(gyvunas1.medzioti())
# print(gyvunas1.prisistatymas())

# class Uzduotis:
#     def __init__(self, pavadinimas, aprasymas):
#         self.pavadinimas = pavadinimas
#         self.aprasymas = aprasymas
#         self.atlikta = False
#
#     def atlikimas(self):
#         self.atlikta = True
#         print(f"Uzduotis '{self.pavadinimas}' buvo atlikta")
#
#     def info(self):
#         return f" Pavadinimas: {self.pavadinimas}\n Aprasymas:{self.aprasymas}"
#
#
# class TodoSarasas:
#     def __init__(self):
#         self.uzduociu_sarasas = []
#
#     def prideti_uzduoti(self, pavadinimas, aprasymas):
#         uzduotis = Uzduotis(pavadinimas, aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print("Uzduociu sarasas yra tuscias")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self, pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas == pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print(f"Uzduotis pavadinimu: '{pavadinimas}' nerasta")
#
# todo_sarasas = TodoSarasas()
#
# while True:
#     print("\nPasirinkite veiksma:")
#     print("1. Prideti uzduoti")
#     print("2. Perziureti uzduotis")
#     print("3. Pazymeti uzduoti kaip atlikta")
#     print("4. Iseiti is uzduociu saraso")
#     pasirinkimas = input("Prasome pasirinkti veiksma_>")
#
#     if pasirinkimas == "1":
#         pavadinimas = input("Iveskite uzduoties pavadinima_>")
#         aprasymas = input("Iveskite uzduoties aprasyma_>")
#         todo_sarasas.prideti_uzduoti(pavadinimas, aprasymas)
#         print("Uzduotis prideta sekmingai!")
#     elif pasirinkimas == "2":
#         todo_sarasas.visos_uzduotys()
#     elif pasirinkimas == "3":
#         pavadinimas = input("Iveskite uzduoties pavadinima, kuria norite pazymeti kaip atlikta_>")
#         todo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas == "4":
#         print("Iseinama...")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")

#sukurti banko saskaita, isimti/ideti pinigus, likucio informacija

# class saskaita:
#     def __init__(self, vardas, pavarde, pradinis_likutis=0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pradinis_likutis = pradinis_likutis
#
#     def inesti_pinigu(self, suma):
#         if suma > 0:
#             self.pradinis_likutis += suma
#         else:
#             print("Klaida, negalima ideti neigiamos sumos")
#
#     def nusiimti_pinigu(self, suma):
#         if suma > 0:
#             if suma <= self.pradinis_likutis:
#                 self.pradinis_likutis -= suma
#                 print(f"Jus sekmingai nusiemete {suma}")
#             else:
#                 print("Klaida, jusu likutis nepakankamas")
#         else:
#             print("Negalite nusiimti neigiamos sumos")
#     def saskaitos_likutis(self):
#         return f"Kliento {self.vardas} {self.pavarde} saskaitos likutis yra {self.pradinis_likutis}"
#
# numeris_vienas = saskaita ("Jonas", "Jonaitis")
#
# numeris_vienas.inesti_pinigu(300)
# numeris_vienas.nusiimti_pinigu(400)
# print(numeris_vienas.saskaitos_likutis())

# Sukurkite Studentas klase kuri reprezentuoja individualų studentą, turintį savo vardą, pavardę, amžių, studento numerį ir pažymių sąrašą.
# Antroje klasėje StudentuValdymoSistema - tai klasė, skirta valdyti studentų sąrašą. Ji leidžia pridėti naujus studentus, gauti informaciją apie konkretų studentą pagal jo numerį ir išvesti visų studentų informaciją.

# class Studentas:
#     def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai=None):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#         self.studento_numeris = studento_numeris
#         self.pazymiai = pazymiai if pazymiai else []
#
#     def studento_vidurkis(self):
#         return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0
#
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#
#     def studento_informacija(self):
#         return (f'Studento vardas {self.vardas}, studento pavarde {self.pavarde}, amzius {self.amzius}, '
#                 f'studento numeris {self.studento_numeris}, pazymiai {self.pazymiai}')
#
#     def pasalinti_pazymi(self,pazymys):
#         if 0 <= pazymys < len(self.pazymiai):
#             del self.pazymiai[pazymys]
#         else:
#             print("Toks pazymys nerastas")
#
# class StudentuValdymoSistema:
#     def __init__(self):
#         self.studentu_sarasas = []
#
#     def prideti_studenta(self, studentas):
#         self.studentu_sarasas.append(studentas)
#         print("Studentas sekmingai pridetas")
#
#     def pasalinti_studenta(self,studento_numeris):
#         naujas_studentu_sarasas = []
#         for s in self.studentu_sarasas:
#             if s.studento_numeris != studento_numeris:
#                 naujas_studentu_sarasas.append(s)
#         self.studentu_sarasas = naujas_studentu_sarasas
#
#     def visi_studentai(self):
#         return self.studentu_sarasas
#
#     def __str__(self):
#         return "\n ".join(str(studentas) for studentas in self.studentu_sarasas)
#
# studentu_sistema = StudentuValdymoSistema()
# studentas1 = Studentas("Jonas", "Jonaitis", 23, 102)
# studentas2 = Studentas("Petras", "Petraitis", 21, 105)
# studentas1.prideti_pazymi(7)
# studentas1.prideti_pazymi(3)
# studentas1.prideti_pazymi(5)
# studentas2.prideti_pazymi(8)
# studentas2.prideti_pazymi(6)
# print(studentas1.studento_informacija())
# studentas1.pasalinti_pazymi(0)
# print(studentas1.studento_informacija())
# print(studentas2.studento_informacija())
# studentu_sistema.pasalinti_studenta(105)
#
# for studentas in studentu_sistema.visi_studentai():
#     print(studentas)









