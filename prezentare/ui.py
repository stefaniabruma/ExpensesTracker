from business.service_cheltuiala import suma_totala_pe_un_tip_dat, ziua_suma_cheltuita_maxima, \
    cheltuielile_cu_suma_data, cheltuieli_sortate_dupa_tip, elimina_cheltuieli_tip_dat, \
    elimina_cheltuieli_mai_mici_suma_data, creeaza_operatie, adauga_operatie_in_undo, numar_operatii_lista, \
    get_nume_operatie, undo_complet
from domeniu.cheltuiala import creeaza_cheltuiala, get_zi_cheltuiala, get_suma_cheltuiala, get_tip_cheltuiala
from domeniu.validator_cheltuiala import valideaza_cheltuiala
from infrastructura.repository_cheltuiala import adauga_cheltuiala_la_lista, set_zi_noua, set_suma_noua, set_tip_nou, \
    get_cheltuieli_mai_mari_decat_o_suma_data, get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data, \
    get_cheltuieli_un_anumit_tip, sterge_cheltuieli_zi_data, sterge_cheltuieli_interval_timp, sterge_cheltuieli_tip_dat, \
    numar_cheltuieli_lista


def print_menu():
    '''
    printeaza optiunile utilizatorului
    :return: nimic, dar printeaza optiunile utilizatorului
    '''
    print("Pentru a introduce o noua cheltuiala introduceti comanda 1")
    print("Pentru a vedea lista de cheltuieli introduceti comanda 2")
    print("Pentru a actualiza o cheltuiala introduceti comanda 3")
    print("Pentru a vedea doar cheltuielile mai mari decat o suma data introduceti comanda 4")
    print("Pentru a vedea doar cheltuielile efectuate inainte de o zi data si mai mici decat o suma data comanda 5")
    print("Pentru a vedea doar cheltuielile de un anumit tip introduceti comanda 6")
    print("Pentru a afisa totalul sumelor cheltuielilor de un anumit tip introduceti comanda 7")
    print("Pentru a afisa ziua/zilele din luna in care s-a cheltuit suma totala maxima introduceti comanda 8")
    print("Pentru a afisa toate cheltuielile ce au o suma data introduceti comanda 9")
    print("Pentru a afisa cheltuielile sortate dupa tip introduceti comanda 10")
    print("Pentru a sterge cheltuielile dintr-o anumita zi introduceti comanda 11")
    print("Pentru a sterge cheltuielile dintr-un anumit interval de timp introduceti comanda 12")
    print("Pentru a sterge cheltuielile de un anumit tip introduceti comanda 13")
    print("Pentru a vedea lista de cheltuieli, dar fara cheltuielile de un anumit tip introduceti comanda 14")
    print("Pentru a vedea lista de cheltuieli, dar fara cheltuielile mai mici decat o suma data introduceti comanda 15")
    print("Pentru a reface ultima operatie efectuata introduceti valoarea 16")

def comanda1(cheltuieli, operatii):
    zi = int(input("Ziua din luna in care s-a efectuat cheltuiala este: "))
    suma = float(input("Suma cheltuita este: "))
    print("Introduceti tipul cheltuielii dintre urmatoarele:\n->mancare\n->intretinere\n->imbracaminte\n->telefon\n->altele")
    tip = input()
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    try:
        valideaza_cheltuiala(cheltuiala)
    except ValueError as ve:
        print(ve)
        return
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    nume_op = "stergere"
    ind_op = numar_cheltuieli_lista(cheltuieli) - 1
    operatie = creeaza_operatie(nume_op, zi, suma, tip, ind_op)
    adauga_operatie_in_undo(operatii, operatie)
    print("Cheltuiala introdusa!")

def comanda2(cheltuieli):
    cnt = 1
    for i in cheltuieli:
        print(cnt, ": ", i)
        cnt += 1

def comanda3(cheltuieli, operatii):
    ind = int(input("Introduceti numarul cheltuielii pe care vreti sa o actualizati: "))
    ind -= 1
    zi_n = int(input("Introduceti ziua noua: "))
    suma_n = float(input("Introduceti suma noua: "))
    tip_n = input("Introduceti noul tip dintre urmatoarele:\n->mancare\n->intretinere\n->imbracaminte\n->telefon\n->altele\n")
    cheltuiala_n = creeaza_cheltuiala(zi_n, suma_n, tip_n)
    try:
        valideaza_cheltuiala(cheltuiala_n)
    except ValueError as ve:
        print(ve)
        return
    nume_op = "actualizare"
    ind_op = ind
    operatie = creeaza_operatie(nume_op, get_zi_cheltuiala(cheltuieli[ind]), get_suma_cheltuiala(cheltuieli[ind]), get_tip_cheltuiala(cheltuieli[ind]), ind_op)
    adauga_operatie_in_undo(operatii, operatie)
    set_zi_noua(cheltuieli[ind], zi_n)
    set_suma_noua(cheltuieli[ind], suma_n)
    set_tip_nou(cheltuieli[ind], tip_n)
    print("Cheltuiala actualizata!")

def comanda4(cheltuieli):
    suma_data = float(input("Suma data este: "))
    try:
        indici = get_cheltuieli_mai_mari_decat_o_suma_data(cheltuieli, suma_data)
    except ValueError as ve:
        print(ve)
        return
    print("Cheltuielile mai mari decat ", suma_data, " sunt:")
    if indici == []:
        print("Nu exista cheltuieli mai mari decat suma introdusa!")
    for i in indici:
        print(i + 1, ": ", cheltuieli[i])

def comanda5(cheltuieli):
    ziua_d = int(input("Ziua data este: "))
    suma_d = float(input("Suma data este: "))

    try:
        indici = get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_d, suma_d)
    except ValueError as ve:
        print(ve)
        return

    if indici == []:
        print("Nu exista cheltuieli care sa fie simultan efectuate inainte de ziua introdusa si mai mici decat suma introdusa!")

    for i in indici:
        print(i + 1, ": ", cheltuieli[i])

def comanda6(cheltuieli):
    tip_d = input(
        "Introduceti tipul cautat dintre urmatoarele:\n->mancare\n->intretinere\n->imbracaminte\n->telefon\n->altele\n")

    try:
        indici = get_cheltuieli_un_anumit_tip(cheltuieli, tip_d)
    except ValueError as ve:
        print(ve)
        return

    if indici == []:
        print("Nu exista cheltuieli cu tipul introdus!")
    for i in indici:
        print(i + 1, ": ", cheltuieli[i])

def comanda7(cheltuieli):
    tip_d = input("Introduceti tipul pentru care vreti sa aflati suma totala cheltuita din urmatoarele:\n->mancare\n->intretinere\n->imbracaminte\n->telefon\n->altele\n")
    try:
        sum = suma_totala_pe_un_tip_dat(cheltuieli, tip_d)
    except ValueError as ve:
        print(ve)
        return
    print("Suma totala pentru tipul <", tip_d, "> este: ", sum)

def comanda8(cheltuieli):
    l_zile = ziua_suma_cheltuita_maxima(cheltuieli)
    print("Ziua/zilele din luna in care s-a cheltuit suma totala maxima este/sunt: ", l_zile)

def comanda9(cheltuieli):
    suma_d = float(input("Introduceti suma pentru care doriti sa vedeti toate cheltuielile: "))
    try:
        indici = cheltuielile_cu_suma_data(cheltuieli, suma_d)
    except ValueError as ve:
        print(ve)
        return

    if indici == []:
        print("Nu exista cheltuieli cu aceasta suma!")
        return
    print("Cheltuielile cu suma ", suma_d, " sunt: ")
    for i in indici:
        print(i + 1, ": ", cheltuieli[i])

def comanda10(cheltuieli):
    indici = cheltuieli_sortate_dupa_tip(cheltuieli)
    for i in indici:
        print(i+1, ": ", cheltuieli[i])

def comanda11(cheltuieli, operatii, nr_stergeri):
    zi_data = int(input("Ziua pentru care doriti sa stergeti cheltuielile este: "))
    copie_cheltuieli = cheltuieli.copy()
    try:
        indici = sterge_cheltuieli_zi_data(cheltuieli, zi_data)
    except ValueError as ve:
        print(ve)
        return
    nume_op = "adaugare"
    for i in indici:
        operatie = creeaza_operatie(nume_op, get_zi_cheltuiala(copie_cheltuieli[i]), get_suma_cheltuiala(copie_cheltuieli[i]), get_tip_cheltuiala(copie_cheltuieli[i]), i)
        adauga_operatie_in_undo(operatii, operatie)

    nr_stergeri.append(len(indici))
    copie_cheltuieli.clear()

    print("Cheltuieli sterse!")

def comanda12(cheltuieli, operatii, nr_stergeri):
    zi_inceput = int(input("Introduceti limita inferioara a intervalului de timp: "))
    zi_sfarsit = int(input("Introduceti limita superioara a intervalului de timp: "))


    copie_cheltuieli = cheltuieli.copy()


    try:
        indici = sterge_cheltuieli_interval_timp(cheltuieli, zi_inceput, zi_sfarsit)
    except ValueError as ve:
        print(ve)
        return

    nume_op = "adaugare"
    for i in indici:
        operatie = creeaza_operatie(nume_op, get_zi_cheltuiala(copie_cheltuieli[i]), get_suma_cheltuiala(copie_cheltuieli[i]), get_tip_cheltuiala(copie_cheltuieli[i]), i)
        adauga_operatie_in_undo(operatii, operatie)

    nr_stergeri.append(len(indici))
    copie_cheltuieli.clear()

    print("Cheltuieli sterse!")

def comanda13(cheltuieli, operatii, nr_stergeri):
    tip_dat = input("Introduceti tipul pentru care vreti sa stergeti toate cheltuielile: ")
    copie_cheltuieli = cheltuieli.copy()
    try:
        indici = sterge_cheltuieli_tip_dat(cheltuieli, tip_dat)
    except ValueError as ve:
        print(ve)
        return
    nume_op = "adaugare"
    for i in indici:
        operatie = creeaza_operatie(nume_op, get_zi_cheltuiala(copie_cheltuieli[i]), get_suma_cheltuiala(copie_cheltuieli[i]), get_tip_cheltuiala(copie_cheltuieli[i]), i)
        adauga_operatie_in_undo(operatii, operatie)

    nr_stergeri.append(len(indici))
    copie_cheltuieli.clear()

    print("Cheltuieli sterse!")

def comanda14(cheltuieli):
    tip_dat = input("Introduceti tipul: ")
    indici = []

    try:
        indici = elimina_cheltuieli_tip_dat(cheltuieli, tip_dat)
    except ValueError as ve:
        print(ve)
        return

    if indici == []:
        print("Nu mai exista cheltuieli de afisat in acest caz!")
        return
    for i in indici:
        print(i+1, ": ", cheltuieli[i])

def comanda15(cheltuieli):
    suma_data = float(input("Suma data este: "))

    try:
        indici = elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data)
    except ValueError as ve:
        print(ve)
        return

    if indici == []:
        print("Nu mai exista cheltuieli de afisat in acest caz!")
        return

    for i in indici:
        print(i+1, ": ", cheltuieli[i])

def comanda16(cheltuieli, operatii, nr_stergeri):
    l = numar_operatii_lista(operatii)

    if operatii == []:
        print("lista goala!\n")
        return

    if get_nume_operatie(operatii[l-1]) == "adaugare":
        u = len(nr_stergeri)
        u = nr_stergeri[u-1]
        while u:
            undo_complet(cheltuieli, operatii)
            u -= 1
        nr_stergeri.remove(nr_stergeri[len(nr_stergeri)-1])
        print("Operatie anulata!\n")
        return
    try:
        undo_complet(cheltuieli, operatii)
    except ValueError as ve:
        print(ve)
        return
    print("Operatie anulata!\n")

def us_in(cheltuieli, operatii, nr_stergeri):
    print_menu()
    comanda = int(input("Introduceti comanda: "))
    if comanda == 1:
        comanda1(cheltuieli, operatii)
    if comanda == 2:
        comanda2(cheltuieli)
    if comanda == 3:
        comanda3(cheltuieli, operatii)
    if comanda == 4:
        comanda4(cheltuieli)
    if comanda == 5:
        comanda5(cheltuieli)
    if comanda == 6:
        comanda6(cheltuieli)
    if comanda == 7:
        comanda7(cheltuieli)
    if comanda == 8:
        comanda8(cheltuieli)
    if comanda == 9:
        comanda9(cheltuieli)
    if comanda == 10:
        comanda10(cheltuieli)
    if comanda == 11:
        comanda11(cheltuieli, operatii, nr_stergeri)
    if comanda == 12:
        comanda12(cheltuieli, operatii, nr_stergeri)
    if comanda == 13:
        comanda13(cheltuieli, operatii, nr_stergeri)
    if comanda == 14:
        comanda14(cheltuieli)
    if comanda == 15:
        comanda15(cheltuieli)
    if comanda == 16:
        comanda16(cheltuieli, operatii, nr_stergeri)