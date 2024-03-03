from domeniu.cheltuiala import get_tip_cheltuiala, get_suma_cheltuiala, creeaza_cheltuiala
from infrastructura.repository_cheltuiala import numar_cheltuieli_lista, set_zi_noua, set_suma_noua, set_tip_nou


def suma_totala_pe_un_tip_dat(cheltuieli, tip_dat):
    '''
    returneaza totalul float al sumelor float ale cheltuielilor din lista cheltuieli care au un anume tip string tip_dat
    :param cheltuieli: lista de cheltuieli
    :param tip_dat: string
    :return: float - totalul sumelor cheltuielilor din lista cheltuieli care au ca tip stringul tip_nou
    '''

    tipuri = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]

    if not (tip_dat in tipuri):
        raise ValueError("tip invalid!\n")

    sum = 0
    for i in cheltuieli:
        if i["tip"] == tip_dat:
            sum = sum + i["suma"]
    return sum

def ziua_suma_cheltuita_maxima(cheltuieli):
    '''
    returneaza ziua/zilele lunii in care s-au afectuat cheltuieli cu cea mai mare suma totala
    :param cheltuieli: lista de cheltuieli
    :return: lista - zilele din luna in care s-au efectuat cheltuieli cu cea mai mare suma totala
    '''
    sum = [0]*31
    maxim = 0
    for i in cheltuieli:
        sum[i["ziua"]] += i["suma"]
        if sum[i["ziua"]] > maxim:
            maxim = sum[i["ziua"]]

    zile = []

    for i in range(1, 31):
        if sum[i] == maxim:
            zile.append(i)
    return zile

def cheltuielile_cu_suma_data(cheltuieli, suma_data):
    '''
    returneaza pozitiile (din lista de cheltuieli cheltuieli) ale cheltuielilor care au suma float suma_data
    :param cheltuieli: lista de cheltuieli
    :param suma_data: float
    :return: lista de indici - care corespund elementelor din lista de cheltuieli cheltuieli care au suma float suma_data
    '''

    if suma_data <= 0:
        raise ValueError("suma invalida!\n")

    indici = []

    cnt = 0
    for i in cheltuieli:
        if i["suma"] == suma_data:
            indici.append(cnt)
        cnt += 1

    return indici

def cheltuieli_sortate_dupa_tip(cheltuieli):
    '''
    returneaza indicii listei cheltuieli intr-o alta ordine astfel incat daca recompunem lista sa obtinem cheltuielile sortate dupa tip astfel: mancare, intretinere, imbracaminte, telefon, altele
    :param cheltuieli: lista de cheltuieli
    :return: lista de indici - indicii elementelor din lista initiala rearanjati astfel incat daca recompunem lista sa obtinem cheltuielile sortate dupa tip
    '''
    tipuri = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]
    indici = []

    for t in tipuri:
        cnt = 0
        for c in cheltuieli:
            if c["tip"] == t:
                indici.append(cnt)
            cnt += 1
    return indici

def elimina_cheltuieli_tip_dat(cheltuieli, tip_dat):
    '''
    returneaza o lista de indici corespunzatori cheltuielillor din lista de cheltuieli cheltuieli care NU au tipul egal cu stringul tip_dat
    :param cheltuieli: lista de cheltuieli
    :param tip_dat: string
    :return: lista - indicii corespunzatori elementelor din lista de cheltuieli cheltuieli care NU au tipul egal cu stringul tip_dat
    '''

    tipuri = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]

    if not(tip_dat in tipuri):
        raise ValueError("tip invalid!\n")

    ind = 0
    indici = []

    for c in cheltuieli:
        if get_tip_cheltuiala(c) != tip_dat:
            indici.append(ind)
        ind += 1

    return indici

def elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data):
    '''
    returneaza indicii cheltuielilor din lista de cheltuieli cheltuieli care NU au suma mai mica decat floatul suma_data
    :param cheltuieli: lista de cheltuieli
    :param suma_data: float
    :return: lista - contine indicii listei de cheltuieli cheltuieli corespunzatori elementelor a caror suma NU este mai mare decat floatul suma_data
    '''

    if suma_data <=0:
        raise ValueError("suma invalida!\n")

    ind = 0
    indici = []

    for c in cheltuieli:
        if get_suma_cheltuiala(c) >= suma_data:
            indici.append(ind)
        ind += 1

    return indici

def creeaza_operatie(nume_op, zi_op, suma_op, tip_op, ind_op):
    '''
    creeaza o opeartie ce are ca nume stringul nume_op, ca zi iintul zi_op, ca suma floatul suma_op, ca tip stringul tip_op)
    :param nume_op: numele operatiei inverse aceleia care s-a efectuat
    :param zi_op: ziua int a cheltuielii pe care s-a efectuat operatia
    :param suma_op: suma float a cheltuielii pe care s-a efectuat operatia
    :param tip_op: tipul string al cheltuielii pe care s-a efectuat operatia
    :return: operatie tip dictionar
    '''

    return {
        'nume': nume_op,
        'zi': zi_op,
        'suma': suma_op,
        'tip': tip_op,
        'indice': ind_op
    }

def get_nume_operatie(operatie):
    '''
    returneaza numele operatiei operatie
    :param operatie: operatie
    :return: numelele string al operatiei operatie
    '''
    return operatie['nume']

def get_zi_operatie(operatie):
    '''
    returneaza ziua cheltuielii pe care s-a efctuat operatie operatie
    :param operatie: operatie
    :return: ziua int a operatiei operatie
    '''
    return operatie['zi']

def get_suma_operatie(operatie):
    '''
    returneaza suma cheltuielii pe care s-a efectuat operatia operatie
    :param operatie: operatie
    :return: suma float a operatiei operatie
    '''
    return operatie['suma']

def get_tip_operatie(operatie):
    '''
    returneaza tipul cheltuielii pe care s-a efectuat operatia operatie
    :param operatie: operatie
    :return: tipul string al operatiei operatie
    '''
    return operatie['tip']

def get_indice_operatie(operatie):
    '''
    returneaz indicele cheltuielii pe care s-a efectuat operatia operatie
    :param operatie:
    :return: indicele int al operatiei operatie
    '''
    return operatie['indice']

def numar_operatii_lista(operatii):
    '''
    returneaza numarul de operatii din lista de operatii
    :param operatii: lista de operatii
    :return: int - numarul de operatii din lista de operatii
    '''
    return len(operatii)

def adauga_operatie_in_undo(operatii, operatie):
    '''
    adauga opusul operatiei efectuate in lista undo
    :param operatii: lista de operatii
    :param operatie: operatie
    :return: lista operatii' = operatii U {operatie}
    '''
    operatii.append(operatie)

def undo_adaugare(cheltuieli, operatii):
    '''
    returneaza lista de cheltuieli de dinainte de efectuarea ultimei operatii in cazul in care ultima operatie a fost de adaugare
    :param cheltuieli: lista de cheltuieli
    :return: cheltuieli' = cheltuieli \ {ultima cheltuiala adugata}
    '''

    if cheltuieli == []:
        raise ValueError("lista goala!\n")

    l = numar_cheltuieli_lista(cheltuieli)
    cheltuieli.remove(cheltuieli[l-1])

    l = numar_operatii_lista(operatii)
    operatii.remove(operatii[l-1])

    return cheltuieli

def undo_actualizare(cheltuieli, operatii):
    '''
    returneaza lista de cheltuieli de dinainte de efectuarea ultimei operatii in cazul in care ultima operatie a fost de actualizare
    :param cheltuieli: lista de cheltuieli
    :param operatii: lista de operatii
    :return: lista de cheltuieli cheltuieli, dar cu ultimul
    '''
    if cheltuieli == []:
        raise ValueError("lista goala!\n")

    l = numar_operatii_lista(operatii)
    zi_noua = get_zi_operatie(operatii[l-1])
    suma_noua = get_suma_operatie(operatii[l-1])
    tip_nou = get_tip_operatie(operatii[l-1])

    ind = get_indice_operatie(operatii[l-1])
    set_zi_noua(cheltuieli[ind], zi_noua)
    set_suma_noua(cheltuieli[ind], suma_noua)
    set_tip_nou(cheltuieli[ind], tip_nou)

    operatii.remove(operatii[l - 1])

    return cheltuieli

def undo_stergere(cheltuieli, operatii):
    '''
    returneaza lista de cheltuieli de dinainte de efectuarea ultimei operatii in cazul in care ultima operatie efectuata e fost de stergere
    :param cheltuieli: lista de cheltuieli
    :param operatii: lista de operatii
    :return: cheltuieli' = cheltuieli U {ultima cheltuiala stearsa}
    '''

    if cheltuieli == []:
        raise ValueError("lista goala!\n")

    l = numar_operatii_lista(operatii)
    zi = get_zi_operatie(operatii[l-1])
    suma = get_suma_operatie(operatii[l-1])
    tip = get_tip_operatie(operatii[l-1])
    indice = get_indice_operatie(operatii[l-1])

    operatii.remove(operatii[l-1])

    cheltuiala = creeaza_cheltuiala(zi, suma, tip)

    cheltuieli.insert(indice, cheltuiala)

    return cheltuieli

def undo_complet(cheltuieli, operatii):
    '''
    returneaza lista de cheltuieli de dinainte de ultima operatie efectuata, indiferent de numele ultimei operatii efectuate
    :param cheltuieli: lista de cheltuieli
    :param operatii: lista de operatii
    :return: lista de cheltuieli cheltuieli de dinainte de ultima operatie efectuata, indiferent de numele acesteia
    '''

    if operatii == []:
        raise ValueError("lista goala!\n")

    l = numar_operatii_lista(operatii)

    if get_nume_operatie(operatii[l-1]) == 'stergere':
        cheltuieli = undo_adaugare(cheltuieli, operatii)
        return cheltuieli

    if get_nume_operatie(operatii[l-1]) == 'actualizare':
        cheltuieli = undo_actualizare(cheltuieli, operatii)
        return cheltuieli

    if get_nume_operatie(operatii[l-1]) == 'adaugare':
        cheltuieli = undo_stergere(cheltuieli, operatii)
        return cheltuieli


