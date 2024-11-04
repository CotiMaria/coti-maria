meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
papanasi_inceput = meniu.count("papanasi")
papanasi_comanda = comenzi.count("papanasi")
pret_papanasi = preturi[0][1]
castig_papanasi = papanasi_inceput * pret_papanasi
print(papanasi_inceput - papanasi_comanda)
print(papanasi_inceput * pret_papanasi)
cata_ceafa_era_la_inceput = meniu.count("ceafa")
cata_ceafa_s_a_comandat = comenzi.count("ceafa")
pret_ceafa = preturi[1][1]
castig_ceafa = cata_ceafa_s_a_comandat * pret_ceafa
print(cata_ceafa_era_la_inceput - cata_ceafa_s_a_comandat)
print(cata_ceafa_era_la_inceput * pret_ceafa)
guias_inceput = meniu.count("guias")
guias_comenzi = comenzi.count("guias")
pret_guias = preturi[2][1]
castig_guias = guias_inceput * pret_guias
castig_cantina = castig_papanasi + castig_ceafa + castig_guias
print(guias_inceput - guias_comenzi)
print(guias_inceput * pret_guias)
print(castig_cantina)
student1 = studenti.pop(0)
comanda1 = comenzi.pop(0)
print(f"Studentul {student1} a comandat {comanda1}")
istoric_comenzi.append([student1,comanda1])
tavi.pop(0)
student2 = studenti.pop(0)
comanda2 = comenzi.pop(0)
print(f"Studentul {student2} a comandat {comanda2}")
istoric_comenzi.append([student2,comanda2])
tavi.pop(1)
student3 = studenti.pop(0)
comanda3 = comenzi.pop(0)
print(f"Studentul {student3} a comandat {comanda3}")
istoric_comenzi.append([student3,comanda3])
tavi.pop(2)
student4 = studenti.pop(0)
comanda4 = comenzi.pop(0)
print(f"Studentul {student4} a comandat {comanda4}")
istoric_comenzi.append([student4,comanda4])
tavi.pop(3)
student5 = studenti.pop(0)
comanda5 = comenzi.pop(0)
print(f"Studentul {student5} a comandat {comanda5}")
istoric_comenzi.append([student5,comanda5])
meniu_set = set(meniu)
disponibilitate = {produs: produs in meniu_set for produs in comenzi}
for produs, exista in disponibilitate.items():
    print(f"Produsul '{produs}'{'exista' if exista else 'nu exista'} in meniu.")
tavi_folosite = 5
tavi_totale = 7
print(tavi_totale - tavi_folosite)
meniu_papanasi = papanasi_inceput - papanasi_comanda
meniu_ceafa = cata_ceafa_era_la_inceput - cata_ceafa_s_a_comandat
meniu_guias = guias_inceput -guias_comenzi
if meniu_papanasi:
    print(" Mai este papanasi: True")
else: print( "Mai este papanasi: False")
if meniu_guias:
    print("Mai este guias: True")
else: print("Mai este guias : False")
if meniu_ceafa:
    print("Mai este ceafa: True")
else: print(" Mai este ceafa: False")
produse_ieftine = []
for produs in preturi:
    nume, pret = produs
    if pret <= 7:
        produse_ieftine.append(nume)
print("Produse din meniu care costă cel mult 7 lei:", produse_ieftine)




