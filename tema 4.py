# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []
print(" ".join(progres))
while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o literă: ").lower()
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja litera aceasta.")
        continue
    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        for i, char in enumerate(cuvant_de_ghicit):
            if char == litera:
                progres[i] = litera
        print("Bravo! Litera se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print("Litera nu se află în cuvânt. Încercări rămase:", incercari_ramase)
    print("Progres:", " ".join(progres))
    print("Încercări rămase:", incercari_ramase)