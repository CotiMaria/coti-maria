
def cauta_document(dosar, numar_referinta):
    n = len(dosar)
    numar_iter = 0
    for i in range(n):
        numar_iter +=1
        if dosar[i] == numar_referinta:
            print(f"Documentul cu numărul de referință {numar_referinta} a fost găsit pe poziția {i} după {numar_iter} documente verificate.")
            return i
    print(f"Documentul cu numărul de referință {numar_referinta} nu a fost găsit. Total documente verificate: {numar_iter}.")
    return -1

import math
def cauta_container(containere, numar_identificare):
    n = len(containere)
    salt = int(math.sqrt(n))
    pasi: int = 0
    st = 0
    while st < n and containere[st] < numar_identificare:
                pasi += 1
                st += salt
    for i in range(st, min(st + salt, n)):
                pasi += 1
                if containere[i] == numar_identificare:
                    print(f"Containerul cu numărul de referință {numar_identificare} a fost găsit pe poziția {i} după {pasi} pași.")
                    return i
    print(f"Containerul cu numărul de referință {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {pasi}.")
    return -1

def cautare_binara(lista, stanga, dreapta, valoare):
    numar_pasi = 0
    while stanga <= dreapta:
        numar_pasi += 1
        mijloc = stanga + (dreapta - stanga)//2
        if lista[mijloc] == valoare:
            return mijloc, numar_pasi
        elif lista[mijloc] < valoare:
            stanga = mijloc +1
        else:
            dreapta = mijloc -1
    return -1, numar_pasi

def cauta_pacient(pacienti, id_pacient):
    n = len(pacienti)
    numar_pasi = 0
    if pacienti[0] == id_pacient:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția 0 după 1 pas de căutare.")
        return 0, 1
    i = 1
    while i < n and pacienti[0] < id_pacient:
        i *= 2
    pozitie, pasi_binari = cautare_binara(pacienti, i// 2, min(i, n-1), id_pacient)
    numar_pasi += pasi_binari
    if pozitie != -1:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția {pozitie} după număr pași de căutare.")
    else:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} nu a fost găsit. Total pași efectuați: {numar_pasi}.")

    return pozitie, numar_pasi





(cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 999))
cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 404)
cauta_container([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_container([1050, 1075, 1100, 1125, 1150, 1175, 1200], 1300)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1100)
