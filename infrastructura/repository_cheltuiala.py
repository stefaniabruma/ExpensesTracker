from domeniu.cheltuiala import get_zi_cheltuiala, get_tip_cheltuiala


def adauga_cheltuiala_la_lista(lista_c, cheltuiala):
    '''
    adauga o noua cheltuiala la lista de cheltuieli deja existente
    :param lista_c: lista de cheltuieli
    :param cheltuiala: cheltuiala
    :return: lista_c' = lista_c U {cheltuiala}
    '''
    lista_c.append(cheltuiala)

def numar_cheltuieli_lista(lista_c):
    '''
    returneaza numarul de cheltuieli din lista lista_c
    :param lista_c: lista
    :return: integer - numarul de cheltuieli din lista_c
    '''
    return len(lista_c)


def set_zi_noua(cheltuiala, zi_noua):
    '''
    modifica ziua int a cheltuielii cheltuiala la noua valoare data de intul zi_noua
    :param cheltuiala: cheltuiala
    :param zi_noua: date
    :return: nimic, dar ziua int a cheltuielii cheltuiala se schimba la intul zi_noua
    '''

    cheltuiala["ziua"] = zi_noua

def set_suma_noua(cheltuiala, suma_noua):
    '''
    modifica suma float a cheltuielii cheltuiala la noua valoare data de float-ul suma_noua
    :param cheltuiala: cheltuiala
    :param suma_noua: float
    :return: nimic, dar suma float a cheltuielii cheltuiala se modifica la floatul suma_noua
    '''

    cheltuiala["suma"] = suma_noua

def set_tip_nou(cheltuiala, tip_nou):
    '''
    modifica tipul string al cheltuielii cheltuiala la noua valoare data de string-ul tip_nou
    :param cheltuiala: cheltuiala
    :param tip_nou: string
    :return: nimic, dar tipul string al cheltuielii cheltuiala se schimba la stringu-ul tip_nou
    '''
    cheltuiala["tip"] = tip_nou

def get_cheltuieli_mai_mari_decat_o_suma_data(cheltuieli, suma_d):
    '''
    returneaza pozitiile (din lista de cheltuieli cheltuieli) ale cheltuielilor care depasesc suma data float suma_d
    :param cheltuieli: lista de cheltuieli
    :param suma_d: float
    :return: o lista de indici ai listei cheltuieli, care corespund acelor elemente ce au suma o valoare strict mai mare decat cea a sumei float suma_d
    '''
    if suma_d <= 0:
        raise ValueError("suma invalida!\n")
    indici = []
    ind = 0
    for i in cheltuieli:
        if i["suma"] > suma_d:
            indici.append(ind)
        ind += 1
    return indici

def get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_data, suma_data):
    '''
    returneaza pozitiile (din lista de cheltuieli cheltuieli) ale cheltuielilor efectuate inainte de o zi data int ziua_data si mai mici decat p suma data float suma_data
    :param cheltuieli: lista de cheltuieli
    :param ziua_data: int
    :param suma_data: float
    :return: o lista de indici ai listei cheltuieli, care corespund acelor elemente care au ziua mai mica decat ziua int ziua_data si suma mai mica decat suma float suma_data
    '''
    errors = ""
    if ziua_data < 1 or ziua_data > 31:
        errors += "zi invalida!\n"
    if suma_data <=0:
        errors += "suma invalida!\n"
    if len(errors) > 0:
        raise ValueError(errors)
    indici = []
    ind = 0
    for i in cheltuieli:
        if i["ziua"] < ziua_data and i["suma"] < suma_data:
            indici.append(ind)
        ind += 1
    return indici

def get_cheltuieli_un_anumit_tip(cheltuieli, tip_dat):
    '''
    returneaza pozitiile (din lista de cheltuieli cheltuieli) ale cheltuielilor care au tipul string tip_dat
    :param cheltuieli: lista de cheltuieli
    :param tip_dat: string
    :return: o lista de indici ai listei cheltuieli, care corespund acelor elemente care au tipul string tip_dat
    '''
    tipuri = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]

    if not(tip_dat in tipuri):
        raise ValueError("tip invalid!\n")

    indici  = []
    ind = 0
    for i in cheltuieli:
        if i["tip"] == tip_dat:
            indici.append(ind)
        ind += 1
    return indici

def sterge_cheltuieli_zi_data(cheltuieli, zi_data):
    '''
    sterge cheltuielile care au ca data ziua int zi_data, returnand lista indicilor corespunzatori elementelor din lista de cheltuieli cheltuieli care au ziua int egala cu valoarea data de intul zi_data
    :param cheltuiala: lista de cheltuieli
    :param zi_data: int
    :return: lista de indici corespunzatori elementelor din lista intitala de cheltuieli cheltuieli care au ziua int egala cu valoarea data de intul zi_data
    '''

    if zi_data < 1 or zi_data > 31:
        raise ValueError("zi invalida!\n")

    indici = []

    i = 0
    lun = numar_cheltuieli_lista(cheltuieli)

    while i<lun:
        if get_zi_cheltuiala(cheltuieli[i]) == zi_data:
                indici.append(i)
        i += 1

    i = 0

    while i < lun:
        if get_zi_cheltuiala(cheltuieli[i]) == zi_data:
            cheltuieli.remove(cheltuieli[i])
            lun -= 1
        else: i += 1

    return indici

def sterge_cheltuieli_interval_timp(cheltuieli, zi_inceput, zi_sfarsit):
    '''
    sterge cheltuielile din lista cheltuieli care au ziua int in intervalul delimitat de int ul zi_inceput si int ul zi_sfarsit inclusiv, returnand lista de indicilor corespunzator elementelor care au fost sterse
    :param cheltuieli: lista de cheltuieli
    :param zi_inceput: int
    :param zi_sfarsit: int
    :return: lista de indici care corespund elementelor din lista intitala cheltuieli care au ziua int aflata in intervalul inchis [zi_inceput, zi_sfarsit]
    '''

    errors = ""

    if zi_inceput < 1 or zi_inceput > 31:
        errors += "Limita inferioara interval invalida!\n"
    if zi_sfarsit < 1 or zi_sfarsit > 31:
        errors += "Limita superioara interval invalida!\n"
    if zi_inceput > zi_sfarsit:
        errors += "Interval invalid!\n"

    if len(errors) > 0:
        raise ValueError(errors)

    i = 0
    lun = numar_cheltuieli_lista(cheltuieli)

    indici = []

    while i <lun:
        if get_zi_cheltuiala(cheltuieli[i]) >= zi_inceput and get_zi_cheltuiala(cheltuieli[i]) <= zi_sfarsit:
                indici.append(i)
        i += 1

    i = 0

    while i < lun:
        if cheltuieli[i]['ziua'] >= zi_inceput and cheltuieli[i]['ziua'] <= zi_sfarsit:
            cheltuieli.remove(cheltuieli[i])
            lun -= 1
        else: i += 1

    return indici

def sterge_cheltuieli_tip_dat(cheltuieli, tip_dat):
    '''
    sterge cheltuielile din lista de cheltuieli care au tipul string egal cu string ul tip_dat, returnand lista de indici corespunzatori elementelor din lista de cheltuieli cheltuieli care au tipul egal cu valorea data de stringul tip_dat
    :param cheltuieli: lista de cheltuieli
    :param tip_dat: string
    :return: lista de indici corespunzatori elementelor din lista intitala de cheltuieli cheltuieli care au tipul egal cu valoarea data de stringul tip_dat
    '''

    tipuri = {'mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele'}

    if not(tip_dat in tipuri):
        raise ValueError("tip invalid!\n")

    i = 0
    lun = numar_cheltuieli_lista(cheltuieli)

    indici = []

    while i < lun:
        if get_tip_cheltuiala(cheltuieli[i]) == tip_dat:
            indici.append(i)
        i += 1

    i = 0

    while i < lun:
        if cheltuieli[i]['tip'] == tip_dat:
            cheltuieli.remove(cheltuieli[i])
            lun -= 1
        else: i += 1

    return indici