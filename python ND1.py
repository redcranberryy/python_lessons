# 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.

# prekes = [
#     {"Pavadinimas": "Rankinukas", "Kaina": 120},
#     {"Pavadinimas": "Pinigine", "Kaina": 70},
#     {"Pavadinimas": "Lagaminas", "Kaina": 165}
# ]

# MARTYNO
# prekes = [
#     {"Pavadinimas": "Rankinukas", "Kaina": 120},
#     {"Pavadinimas": "Pinigine", "Kaina": 70},
#     {"Pavadinimas": "Lagaminas", "Kaina": 165}
# ]
# a = prekes[0]
# b = prekes[1]
# c = prekes[2]
#
# verte = max(a["Kaina"],b["Kaina"],c["Kaina"])
# if a["Kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {a["Pavadinimas"]}')
# if b["Kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {b["Pavadinimas"]}')
# if c["Kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {c["Pavadinimas"]}')

# 2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas išlaikė egzaminą;

# studentas = {
#     "Vardas": "Jonas",
#     "Pazymys": 7
# }
#
# if studentas ['Pazymys'] >= 5:
#     print ("Studentas islaike egzamina")
# else:
#     print ("Studentas neislaike egzamino")

# MARTYNO VARIANTAS
# studento_pazymiai = {
#     "Matematika": 7,
#     "Anglu": 4,
#     "Geografija": 9
# }
#
# if studento_pazymiai["Matematika"] < 5:
#     print('Matematikos neislaike')
# else:
#     print('Matematika islaike')
# if studento_pazymiai['Anglu'] < 5:
#     print('Anglu neislaike')
# else:
#     print('Anglu islaike')
# if studento_pazymiai['Geografija'] < 5:
#     print('Geografijos neislaike')
# else:
#     print('Geografija islaike')

# 3. Sukurkite žodyną su kliento informacija ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.

# klientas = {
#     "vardas": "Petras",
#     "saskaitos_suma": 237,
#     "pirkinio_kaina": 125
# }
#
# if klientas["saskaitos_suma"] < klientas["pirkinio_kaina"]:
#     print("lesu_nepakanka")
# else:
#     print("galima pirkti")

# 4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles: pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

# ROSVALDO
#
# pajamos = 1345
#
# if pajamos > 5000:
#     print("Mokesciu suma", + pajamos * 0.2)
# elif pajamos > 1000:
#     print("Mokesciu suma", + pajamos * 0.15)
# elif pajamos > 0:
#     print("Mokesciu suma", + pajamos * 0.1)
# else:
#     print("Pajamu nera")

