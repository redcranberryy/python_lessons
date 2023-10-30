# ''' Multi-komentaras''' - su trim kabutem priekyje ir pabaigoje

# vardas = "Jonas"
# amzius = 30
# ar_jonas_moka_programuoti = False
# jono_pirkiniu_krepselio_suma = 34.5

# print(type(vardas)) - patikrinti, kokios rusies rodiklis yra (str, int, bool, float)

# print("Mano draugo vardas yra " + vardas + " jo amzius ", amzius, ar_jonas_moka_programuoti, jono_pirkiniu_krepselio_suma)

# listas(array) masyvas = [] - lauztiniai skliaustai

# vaisiai = ["Obuolys", "Arbuzas", "Bananas", "Kriause"]
# ilgis = len(vaisiai) - kiek eilutej yra reiksmiu
# print(ilgis)
# print(vaisiai [1]) - reiksmes prasideda nuo 0 - Obuolys 0, Arbuzas 1 ir t.t.
# print(vaisiai[:2]) - rodo pirmas dvi reiksmes slicinimas ima reiksmes nuo 1
# print(vaisiai[::2]) -  paima kas antra reiksme
# pridedame_vaisiu = vaisiai.append("Melionas") - append prideda reiksme gale (galima rasyt be kintamojo)
# print(vaisiai) - atnaujinta sarasa atsispausdinam
# vaisiai.insert(0,"Melionas") - prideti objekta i ta vieta, kuria norime
# print(vaisiai)
# keiciam_reiksme = vaisiai [1] = "Kivis" - pakeiciame Arbuza i Kivi
# print(vaisiai)
# indeksas = vaisiai.index("Bananas") #- surasti, koks tam tikro objekto indeksas
# print(indeksas)
# vaisiai.remove("Kriause") - istrina tam tikra reiksme is eilutes
# print(vaisiai)
# vaisiai.pop(2)
# print(vaisiai)
# print(vaisiai[1]) - spausdina reiksme, kuria buvome pries tai apibreze
# print(vaisiai)

# dictionary - structure = my_dict = {key1:value1, key2:value2}
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# # print(zodynas["Vardas"]) - atspausdinam varda
#
# zodynas["ar_studentas"] = True #- pridedame, ar studentas su reiksle
# print(zodynas)

# del zodynas["Miestas"] - pasalina kazkokia reiksme is eilutes
# print(zodynas)

# studentai = {
#     "Jonas":{
#         "Amzius": 32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#     },
#     "Ona": {
#         "Amzius": 25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#     },
#     "Antanas": {
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#     }
# }
# print(type(studentai))
# print(studentai["Jonas"])

# studentai = [
#     {   "Vardas": "Jonas",
#         "Amzius": 32,
#         "Miestas": "Kaunas",
#         "Profesija": "Inzinierius"
#     },
#     {   "Vardas": "Ona",
#         "Amzius": 25,
#         "Miestas": "Klaipeda",
#         "Profesija": "Gydytoja"
#     },
# {       "Vardas": "Antanas",
#         "Amzius": 46,
#         "Miestas": "Vilnius",
#         "Profesija": "Mokytojas"
#     }
# ]

# print(studentai)
# print(studentai[0]) - varda idejome i vidu (keiciasi ir isoriniai skliaustai) ir todel rezultate rodo ir varda

# naujas_studentas = {
#         "Vardas": "Petras",
#         "Amzius": 36,
#         "Miestas": "Kaunas",
#         "Profesija": "Siuvejas"
# }
# studentai.append(naujas_studentas) - susikureme nauja studenta, pridejome i lentele ir atspausdinom viska su nauju studentu
# print(studentai)

# if salyga if salyga: jusu veiksmai;

# amzius = 15
# if amzius >= 18:
#     print("Asmuo yra pilnametis")
# elif amzius > 13:
#     print ("Asmuo yra paauglys")
# else:
#     print("Asmuo nera pilnametis")

# amzius = 40
# if not amzius < 18:
#     print("Asmuo yra paauglys")
# elif amzius > 18:
#     print ("Asmuo yra pilnammetis")
# else:
#     print("Asmuo yra vaikas")

# vaisiai = ["bananas", "kivis", "obuolys"]
# if "kivis" in vaisiai:
#     print("Vaisius kivis")
# elif not "kivis" in vaisiai:
#     print("Vaisius nerastas")
# else:
#     print("Vaisiu sarasas tuscias")

# vaisiai = []
# if not vaisiai:
#     print("Vaisiu sarasas tuscias")
# elif "kivis" in vaisiai:
#     print("Vaisius kivis")
# else:
#     print("Vaisius nerastas")

# age = 18
# has_id = False
#
# if age >= 18:
#     if has_id:
#         print("Gali balsuoti")
#     else:
#         print ("Jums reikia asmens tapatybes korteles")
# else:
#     print("Jums dar negalima balsuoti")
#
# prekiu_kategorijos = ['Vaisiai', 'Mesa', 'Darzoves']
# print(f'Mano parduotuves prekiu kategorijos "{prekiu_kategorijos}" is kuriu galite rinktis') #- f - formatavimas, kai iterpia prekiu tipo reiksmas. jei nera f - neiterps.
#
# prekes = {
#     'Vaisiai': ['Obuoliai','Bananai'],
#     'Mesa': ['Kiauliena','Vistiena'],
#     'Darzoves': ['Bulves','Pomidorai']
# }
# #norime rasti prekes kategorija "Mesa" ir preke "Vistiena"
#
# norima_kategorija = 'Mesa'
# norima_preke = 'Vistiena'
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_preke in prekes[norima_kategorija]:
#         print(f"Parduotuveje yra {norima_preke}")
#     else:
#         print(f"Parduotuveje nera {norima_preke}")
# else:
#     print(f"Parduotuveje nera prekiu kategorijos: {norima_kategorija}")



# 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
#
# zmones = [
#     {
#     "Vardas": "Tomas",
#     "Amzius": 12
#     },
#     {
#     "Vardas": "Inga",
#     "Amzius": 43
#     },
#     {
#     "Vardas": "Petras",
#     "Amzius": 17
#     }
# ]
# print(zmones)

#2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi: "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).

# zmogus = zmones[2]
#
# if zmogus ['Amzius'] > 18:
#     print(f' Sis zmogus {zmogus["Vardas"]} yra pilnametis')
# elif zmogus == 18:
#     print(f' Sis zmogus {zmogus["Vardas"]} yra nepilnametis')
# else:
#     print(f' Sis zmogus {zmogus["Vardas"]} yra vaikas')


# zodynas = [
#     {
#     "Vardas": "Tomas",
#     "Atlyginimas": 3000,
#     "Pareigos": "Inzinierius"},
#     {
#     "Vardas": "Inga",
#     "Atlyginimas": 2000,
#     "Pareigos": "Buhaltere"},
#     {
#     "Vardas": "Petras",
#     "Atlyginimas": 4000,
#     "Pareigos": "Direktorius"}
# ]

# print(zodynas)

# 2 užduotis:
# 1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
# 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"), padidinkite jo atlyginimą 10%. Jei jis nėra "inžinierius", palikite atlyginimą nepakeistą.

# darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 3000,
#     "Pareigos": "Inzinierius"
#     }
#
# # print(darbuotojas)
#
# # == lyginimas
# # = priskyrimas
#
# if darbuotojas["Pareigos"] == "Inzinierius":
#     #padidinti 10proc atlyginima / ilgesnis uzrasymas
#     # darbuotojas["Atlyginimas"] = darbuotojas["Atlyginimas"] * 1.10
#     #padidinti 10proc atlyginima / trumpesnis uzrasymas
#     # darbuotojas["Atlyginimas"] *= 1.10 - padaugina is kiek reikia
#     # darbuotojas["Atlyginimas"] += 100 - prideda 100
#     # darbuotojas["Atlyginimas"] -= 100 - atima 100
#
# print(darbuotojas)


# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;

# knygos = [
#     {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo metai": 2002}
# ]
#
# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus, kuriu ieskote_>"))
# knyga = knygos[0]
# # print(knyga_pagal_ieskomus_metus)
#
# if knyga["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knyga['pavadinimas']}")

#Papildoma salyga sugalvojom:
# if knyga ["isleidimo metai"] != knyga_pagal_ieskomus_metus:
#     print("Tokia knyga nerasta")
# arba:
# else:
#     print("Tokia knyga nerasta")

# ARBA

# knygos = [
#     {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo metai": 2002}
# ]
#
# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus, kuriu ieskote_>"))
#
# if knygos[0]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
# elif knygos[1]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[1]['pavadinimas']}")
# elif knygos[2]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[2]['pavadinimas']}")
# else:
#     print(f"Deja, knygu, isleistu {knyga_pagal_ieskomus_metus} metais, nera")


# knygos = [
#     {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo metai": 2002}
# ]
# try:
#     knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus, kuriu ieskote_>"))
#
#     if knygos[0]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
#     elif knygos[1]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[1]['pavadinimas']}")
#     elif knygos[2]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[2]['pavadinimas']}")
#     else:
#         print(f"Deja, knygu, isleistu {knyga_pagal_ieskomus_metus} metais, nera")
# except ValueError:
#     print("Blogas ivesties formatas")

# Importuojamos bibliotekos VISUOMET rasomos pirmose eilutese

# import os
#
# dabartinis_katalogas = os.getcwd()
#
# print(dabartinis_katalogas)
# norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norite matyti_>")
#
# try:
#     #bandome gauti aplanko turini
#     turinys = os.listdir(norimas_aplankas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja, aplankas '{norimas_aplankas}' nerastas")

# import os
#
# dabartinis_katalogas = os.getcwd()
# # print(dabartinis_katalogas)
# # norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norite matyti_>")
# naujas_katalogas = input("Prasome nurodyti katalogo lokacija_>")
#
# try:
#     keiciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Dabartinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja, aplankas '{naujas_katalogas}' nerastas")

import os
import shutil

# EXTENSION_MAP ={
#     '.jpg': "Images",
#     '.jpeg': "Images",
#     '.png': "Images",
#     '.gif': "Images",
#     ".pdf": "Documents",
#     ".txt": "Documents"
# }
#
# filename = input("Please write the name of the file you want to organize_> ")
#
# file_extension = os.path.splitext(filename)[1]
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#         #jei tokios direktorijos nerasime, turesime ja sukurti
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#         shutil.move(filename, os.path.join(directory_name, filename))
#         print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("The file does not exist or its extension is not recognized")
# except FileNotFoundError:
#     print(f"Error: {filename} was not found")
# except PermissionError:
#     print(f"Error: You don't have permissions to move '{filename}'")
#




