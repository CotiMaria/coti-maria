
def cauta_document(dosar, numar_referinta):
    n = len(dosar)
    numar_iter = 0
    for i in range(n):
        numar_iter +=1
        if dosar[i] == numar_referinta:
            print(f"Documentul cu numărul de referință {numar_referinta} a fost găsit pe poziția {i} după {numar_iter} documente verificate.")
            return i
    print(f"Documentul cu numărul de referință {numar_referinta} nu a fost găsit în dosar. Total documente verificate: {numar_iter}.")
    return -1

import math
def cauta_container(containere, numar_identificare):
    n = len(containere)
    salt = int(math.sqrt(n))
    pasi: int = 0
    for i in range(0, n, salt):
                pasi += 1
                if containere[i] < numar_identificare:
                    st = i
                elif containere[i] == numar_identificare:
                    print(f"Containerul cu numărul {numar_identificare} a fost găsit pe poziția {i} după {pasi} pași.")
                    return i
                else:
                    break
    for i in range(st, min(st + salt, n)):
                pasi += 1
                if containere[i] == numar_identificare:
                    print(f"Containerul cu numărul {numar_identificare} a fost găsit pe poziția {i} după {pasi} pași.")
                    return i
    print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {pasi}.")
    return -1

def cautare_binara(lista, stanga, dreapta, valoare):
    global numar_iteratii
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
    global numar_iteratii
    n = len(pacienti)
    numar_pasi = 0
    if pacienti[0] == id_pacient:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția 0 după 0 pași de căutare.")
        return 0, 1
    i = 1
    while i < n and pacienti[i] < id_pacient:
        numar_pasi += 1
        i *= 2
    pozitie, pasi_binari = cautare_binara(pacienti, i// 2, min(i, n-1), id_pacient)
    numar_pasi += pasi_binari
    if pozitie != -1:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția {pozitie} după {numar_pasi} pași de căutare.")
    else:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} nu a fost găsit. Total pași efectuați: {numar_pasi}.")

    return pozitie, numar_pasi
def gaseste_cnp(cnpuri, data_nașterii):
    for cnp in cnpuri:
        data_in_cnp = cnp[1:7]
        if data_in_cnp == data_nașterii:
            print(f"Primul CNP găsit pentru data de naștere {data_nașterii} este {cnp}.")
            return 0
    print(f"Nu s-a găsit niciun CNP pentru data de naștere {data_nașterii}.")
    return -1





(cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 999))
cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 404)
cauta_container([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_container([1050, 1075, 1100, 1125, 1150, 1175, 1200], 1300)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1100)
gaseste_cnp(["1970101223456", "1980050523456", "1990050523456", "2000010123456"], "001001")
