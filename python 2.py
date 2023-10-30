#for yra raktas sekoje
#print(ranktas)

# for i in range(5):
#     print("Skaicius", i)

# skaiciai = [1,2,3,4,5]
#
# for skaicius in skaiciai:
#     print("Mano saraso skaicius", skaicius)

# tekstas = "Python data science"
# for raide in tekstas:
#     print(raide)

# zodynas = {"a":1, "b":2, "c":3}
#
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])


# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         break
#     print(skaicius)

# sarasas = [1, 2, 3, 4, 5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         continue
#     print(skaicius)

# skaiciai = [10,20,30,40,50]
# #
# suma = sum(skaiciai)
# print(suma)
# #
# vidurkis = suma /len(skaiciai)
# print("Gautas vidurkis", vidurkis)
#
# for skaicius in skaiciai:
#     if skaicius >= vidurkis:
#         print (skaicius)

# sarasas su vardais, reikia atspausdinti kiekviena varda atskiroje eiluteje

# sarasas = ["Jonas","Petras","Ona","Marija"]
#
# for vardas in sarasas:
#     print(vardas)

# sarasas = ["Jonas","Petras","Ona","Marija"]
#
# for vardas in sarasas:
#     print(vardas+'\n')

# sarasas = ["Jonas","Petras","Ona","Marija"]
# print('\n'.join(sarasas))

#atspausdinti zodi python atvirksciai - nohtyp
# tekstas_1 = "python"
# tekstas_2 = ""
# for raide in tekstas_1:
#     tekstas_2 = raide + tekstas_2
#     print(tekstas_2)

# atspausdinti visa daugybos lentele
#
# max_skaicius = 10
# for i in range(1,max_skaicius+1):
#     for j in range(1,max_skaicius+1):
#         print(i*j,end="\t") # (\t - reiskia tarpa)
#     print()

#pasirasyri lista, kuriame butu tekstas ir zodziai yra atskirti i atskirus indeksus. Ispausdinti zodzius sujungus

# sarasas = ["Labas","rytas","mieli","mokiniai"]
# # print(sarasas)
# for zodis in sarasas:
#     print(zodis)

# sarasas = ["Labas ", "rytas ", "mieli ", "mokiniai "]
# # print(sarasas)
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 = sarasas_2 + zodis
# print(sarasas_2, end="\t")

# sarasas = ["Labas", "rytas", "mieli", "mokiniai"]
# # print(sarasas)
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 += zodis+" " #kabutes su tarpu, kad tarp zodziu atsirastu tarpai
# sujungtas_tekstas = sarasas_2.rstrip() #-pasalina tarpa po paskutinio zodzio
# print(sujungtas_tekstas)

# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ")



# skaicius = 1
#
# while skaicius <= 20:
#     print(skaicius)
    # skaicius += 1

# ivestis = int(input("Iveskite teigiama skaiciu_>"))
# while ivestis < 0:
#     print("Jusu skaicius neigiamas")
#     ivestis = int(input("Bandykite dar karta_>"))
# print("Ivedete teigiama skaiciu")

# atsakymas = 5
# spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
#
# while spejimas != atsakymas:
#     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta_>"))
# print("Sveikiname, atspejote!")

# while True:
#     print("-----Meniu-----")
#     print("1. Atspausdinti pasveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3)_>")
#     if pasirinkimas == "1":
#         print(f"Labas!")
#     elif pasirinkimas == "2":
#         vardas = input("Iveskite nauja varda_>")
#         print("Sekmingai ivedete nauja varda!")
#         print(f"Jusu vardas pakeistas i {vardas}")
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI")
#         break
#     else:
#         print("Netetisingas pasirinkimas! Bandykite dar karta")

# ar_veikia = True
# while ar_veikia:
#     print("-----Meniu-----")
#     print("1. Atspausdinti pasveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3)_>")
#     if pasirinkimas == "1":
#         print(f"Labas!")
#     elif pasirinkimas == "2":
#         vardas = input("Iveskite nauja varda_>")
#         print("Sekmingai ivedete nauja varda!")
#         print(f"Jusu vardas pakeistas i {vardas}")
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI")
#         ar_veikia = False
#     else:
#         print("Netetisingas pasirinkimas! Bandykite dar karta")

# parasyti programa, kurioje nurodytas paslaptingas zodis, jei neatspeja, programa turi is naujo pasileisti, tol kol atspes zodi

# paslaptingas_zodis = "saldainis"
# spejimas = input("Spekite paslaptingaji zodi_>")
#
# while spejimas != paslaptingas_zodis:
#     spejimas = input("Neteisingas atsakymas! Bandykite dar karta_>")
# print("Sveikiname, atspejote!")

# programa, kurioje irasau skaiciu ir man turi ismesti to skaiciaus daugybos lentele


# pasirinkimas = int(input("Pasirinkite skaiciu nuo 1 iki 10_>"))
# max_skaicius = 1
# while max_skaicius <=10:
#     rezultatas = max_skaicius * pasirinkimas
#     print(f'{pasirinkimas} * {max_skaicius} = {rezultatas}')
#     max_skaicius +=1

# FUNKCIJOS

#sintakse funkcijose: def funkcijosPavadinimas(argumentai):
#Jusu kodas

# def pasisveikinti():
#     print("Helloo Python")
# pasisveikinti()
#
# Arba
# if __name__ == '__main__': #visada tas pats parasymas
#     pasisveikinti()

# def pasisveikinti(vardas):
#     print(f"Helloo {vardas}")
# pasisveikinti("Margarita")

# def suma(a,b):
#     return a + b
#
# atsakymas = suma(5,3)
# print(atsakymas)

# susikursime knygu valdymo sistema

# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knyga")
#     print("2. Perziureti visas knygas")
#     print("3. Ieskoti knygos pagal pavadinima")
#     print("4. Iseiti")

# rodyti_meniu()

# Pridedame knyga

# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskite knygos autoriu_>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas, "autorius": autorius})
#     print(f"knyga '{pavadinimas}' prideta!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"pavadinimas: {knyga['pavadinimas']}, autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima, kurios ieskote_>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"pavadinimas: {knyga['pavadinimas']}, autorius: {knyga['autorius']}")
#     else:
#         print(f"Knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-4)_>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 4_>")
#
# if __name__ == '__main__':
#     main()

# Bankine sistema / idet pinigus, isimt pinigus, suzinoti balansa

# def rodyti_meniu():
#     print("\n-----Mini Banko sistema-----")
#     print("1. Atidaryti nauja saskaita")
#     print("2. Inesti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Perziureti saskaitos likuti")
#     print("5. Uzdaryti saskaita")
#     print("6. Iseiti")
#
# # rodyti_meniu()
#
# banko_saskaitos = {
# }
#
# def atidaryti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite kliento varda_>")
#     pradinis_likutis = int(input("Iveskite pradini likuti_>"))
#     saskaitos_numeris = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_numeris] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja saskaita '{saskaitos_numeris}' prideta!")
#
# def inesti_pinigus(paslaugos):
#     saskaitos_numeris = int(input("Iveskite saskaitos numeri_>"))
#     suma = float(input("Iveskite inesamu pinigu suma_>"))
#     banko_saskaitos[saskaitos_numeris]["pradinis_likutis"] += suma
#     print(f"I saskaita nr.: '{saskaitos_numeris}' sekmingai inesta '{suma}' eurai")
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_numeris = int(input("Iveskite saskaitos numeri_>"))
#     suma = float(input("Iveskite nusiimamu pinigu suma_>"))
#     banko_saskaitos[saskaitos_numeris]["pradinis_likutis"]
#     if suma <= banko_saskaitos[saskaitos_numeris]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_numeris]["pradinis_likutis"] -= suma
#         print(f"Is saskaitos nr.: '{saskaitos_numeris}' sekmingai nusiimta '{suma}' eurai")
#     else:
#         print(f"Likutis nepakankamas")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_numeris = int(input("Iveskite saskaitos numeri_>"))
#     likutis = banko_saskaitos[saskaitos_numeris]["pradinis_likutis"]
#     print(f"Saskaitos nr.: '{saskaitos_numeris}' likutis yra '{likutis}' eurai")
#
# def uzdaryti_saskaita(paslaugos):
#     saskaitos_numeris = int(input("Iveskite saskaitos numeri_>"))
#     del banko_saskaitos[saskaitos_numeris]
#     print(f"Banko saskaita nr.: '{saskaitos_numeris}' sekmigai uzdaryta")
#
# def main():
#     paslaugos = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-6)_>")
#         if pasirinkimas == "1":
#             atidaryti_saskaita(paslaugos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(paslaugos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(paslaugos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(paslaugos)
#         elif pasirinkimas == "5":
#             uzdaryti_saskaita(paslaugos)
#         elif pasirinkimas == "6":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6_>")
#
# if __name__ == '__main__':
#     main()

# Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# BLOGAS VARIANTAS:
# def pvm_skaiciuokle (kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print(kaina_su_pvm)
#
# kaina_be_pvm = int(input("Iveskite kaina be PVM_>"))
# pvm_skaiciuokle(kaina_be_pvm)

# def pvm_skaiciuokle (kaina):
#     print(f"Kaina su PVM yra {kaina * 1.21} eurai")
# kaina_be_pvm = int(input("Iveskite kaina be PVM_>"))
# pvm_skaiciuokle(kaina_be_pvm)


# def be_pvm(kaina):
#     return kaina * 1.21
#
# kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
# print("Kaina su PVM", + kaina_su_pvm)