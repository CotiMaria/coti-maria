meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
papanasi_inceput = meniu.count("papanasi")
papanasi_comanda = comenzi.count("papanasi")
pret_papanasi = preturi[1][0]
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
print(guias_inceput - guias_comenzi)
print(guias_inceput * pret_guias)
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
for produs, exista in disponibilitate.items()
    print(f"Produsul '{produs}'{'exista' if exista else 'nu exista'} in meniu.")
tavi_folosite = 5
tavi_totale = 7
print(tavi_totale - tavi_folosite)
 mancare_ieftina = []
        for mancare_pret in preturi:
            pret_mancare = mancare_pret[1]
            nume_mancare = mancare_pret[0]
            if pret_mancare <= 7:
                mancare_ieftina.append(nume_mancare)
                print(mancare_ieftina)
                print(len(mancare_ieftina))



