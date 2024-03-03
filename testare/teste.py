from business.service_cheltuiala import suma_totala_pe_un_tip_dat, ziua_suma_cheltuita_maxima, \
    cheltuielile_cu_suma_data, cheltuieli_sortate_dupa_tip, elimina_cheltuieli_tip_dat, \
    elimina_cheltuieli_mai_mici_suma_data, adauga_operatie_in_undo, creeaza_operatie, get_nume_operatie, \
    get_zi_operatie, get_suma_operatie, get_tip_operatie, numar_operatii_lista, undo_adaugare, undo_actualizare, \
    get_indice_operatie, undo_stergere, undo_complet
from domeniu.cheltuiala import creeaza_cheltuiala, get_zi_cheltuiala, get_suma_cheltuiala, get_tip_cheltuiala
from domeniu.validator_cheltuiala import valideaza_cheltuiala
from infrastructura.repository_cheltuiala import set_zi_noua, set_suma_noua, set_tip_nou, numar_cheltuieli_lista, \
    adauga_cheltuiala_la_lista, get_cheltuieli_mai_mari_decat_o_suma_data, \
    get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data, get_cheltuieli_un_anumit_tip, sterge_cheltuieli_zi_data, \
    sterge_cheltuieli_interval_timp, sterge_cheltuieli_tip_dat


def ruleaza_teste_cheltuiala():
    zi = 22
    suma = 500.0
    tip = "intretinere"

    cheltuiala = creeaza_cheltuiala(zi, suma, tip)

    assert zi == get_zi_cheltuiala(cheltuiala)
    assert abs(suma - get_suma_cheltuiala(cheltuiala)) < 0.001
    assert tip == get_tip_cheltuiala(cheltuiala)



def ruleaza_teste_validator_cheltuiala():
    zi = 20
    suma = 500.0
    tip = "intretinere"

    cheltuiala_corecta = creeaza_cheltuiala(zi, suma, tip)
    valideaza_cheltuiala(cheltuiala_corecta)

    zi_gresita = 32
    suma_gresita = -45.3
    tip_gresit = "chirie"

    cheltuiala_gresita = creeaza_cheltuiala(zi_gresita, suma_gresita, tip_gresit)

    try:
        valideaza_cheltuiala(cheltuiala_gresita)
        assert False
    except ValueError as ve:
        assert str(ve) == "zi invalida!\nsuma invalida!\ntip invalid!\n"



def ruleaza_teste_repository_cheltuiala():
    cheltuieli = []
    assert numar_cheltuieli_lista(cheltuieli) == 0

    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)

    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    assert numar_cheltuieli_lista(cheltuieli) == 1

    zi_noua = 21
    suma_noua = 600.1
    tip_nou = "mancare"

    set_zi_noua(cheltuiala, zi_noua)
    assert get_zi_cheltuiala(cheltuiala) == zi_noua

    set_suma_noua(cheltuiala, suma_noua)
    assert get_suma_cheltuiala(cheltuiala) == suma_noua

    set_tip_nou(cheltuiala, tip_nou)
    assert get_tip_cheltuiala(cheltuiala) == tip_nou

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 26
    suma = 17.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi_d = 1
    assert sterge_cheltuieli_zi_data(cheltuieli, zi_d) == []
    assert cheltuieli == [{'ziua': 21, 'suma': 600.1, 'tip': 'mancare'}, {'ziua': 21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 23, 'suma': 66.3, 'tip': 'mancare'}, {'ziua': 26, 'suma': 17.3, 'tip': 'mancare'}]

    zi_d = 21
    assert sterge_cheltuieli_zi_data(cheltuieli, zi_d) == [0, 1]
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 23, 'suma': 66.3, 'tip': 'mancare'}, {'ziua': 26, 'suma': 17.3, 'tip': 'mancare'}]

    zi_d = 23
    assert sterge_cheltuieli_zi_data(cheltuieli, zi_d) == [1]
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 26, 'suma': 17.3, 'tip': 'mancare'}]

    zi_d = 0
    try:
        sterge_cheltuieli_zi_data(cheltuieli, zi_d)
        assert False
    except ValueError as ve:
        assert str(ve) == "zi invalida!\n"

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 600.1
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi_inceput = 4
    zi_sfarsit = 10


    assert sterge_cheltuieli_interval_timp(cheltuieli, zi_inceput, zi_sfarsit) == []
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 26, 'suma': 17.3, 'tip': 'mancare'}, {'ziua': 23, 'suma': 66.3, 'tip': 'mancare'}, {'ziua': 21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 21, 'suma': 600.1, 'tip': 'mancare'}]

    zi_inceput = 20
    zi_sfarsit = 30

    assert sterge_cheltuieli_interval_timp(cheltuieli, zi_inceput, zi_sfarsit) == [1, 2, 3, 4]
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]

    zi_inceput = 32
    zi_sfarsit = -1

    try:
        sterge_cheltuieli_interval_timp(cheltuieli, zi_inceput, zi_sfarsit)
        assert False
    except ValueError as ve:
        assert str(ve) == "Limita inferioara interval invalida!\nLimita superioara interval invalida!\nInterval invalid!\n"

    zi = 26
    suma = 17.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 600.1
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    tip_dat = "altele"

    assert sterge_cheltuieli_tip_dat(cheltuieli, tip_dat) == []
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 26, 'suma': 17.3, 'tip': 'mancare'}, {'ziua': 23, 'suma': 66.3, 'tip': 'mancare'}, {'ziua': 21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 21, 'suma': 600.1, 'tip': 'mancare'}]

    tip_dat = "mancare"

    assert sterge_cheltuieli_tip_dat(cheltuieli, tip_dat) == [1, 2, 3 , 4]
    assert cheltuieli == [{'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]

    tip_dat = "mancarw"

    try:
        sterge_cheltuieli_tip_dat(cheltuieli, tip_dat)
        assert False
    except ValueError as ve:
        assert str(ve) == "tip invalid!\n"


def ruleaza_teste_cautari_cheltuiala():
    cheltuieli = []

    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    suma_data = 99.9

    assert get_cheltuieli_mai_mari_decat_o_suma_data(cheltuieli, suma_data) == [0, 1]

    suma_data = 1001.2

    assert get_cheltuieli_mai_mari_decat_o_suma_data(cheltuieli, suma_data) == []

    suma_data = -1

    try:
        get_cheltuieli_mai_mari_decat_o_suma_data(cheltuieli, suma_data)
        assert False
    except ValueError as ve:
        assert str(ve) == "suma invalida!\n"

    suma_data = 100.3
    ziua_data = 21

    assert get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_data, suma_data) == [2]

    suma_data = 520.0

    assert get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_data, suma_data) == [0, 2]

    suma_data = 10.1

    assert get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_data, suma_data) == []

    suma_data = -2
    ziua_data = 32

    try:
        get_cheltuieli_mai_mici_decat_o_zi_si_o_suma_data(cheltuieli, ziua_data, suma_data)
        assert False
    except ValueError as ve:
        assert str(ve) == "zi invalida!\nsuma invalida!\n"

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    tip_dat = "mancare"
    assert get_cheltuieli_un_anumit_tip(cheltuieli, tip_dat) == [1, 3]

    tip_dat = "telefon"
    assert get_cheltuieli_un_anumit_tip(cheltuieli, tip_dat) == []

    tip_dat = "altelr"

    try:
        get_cheltuieli_un_anumit_tip(cheltuieli, tip_dat)
        assert False
    except ValueError as ve:
        assert str(ve) == "tip invalid!\n"


def ruleaza_teste_rapoarte_cheltuiala():
    cheltuieli = []
    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 26
    suma = 17.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)


    tip_dat = "mancare"
    assert suma_totala_pe_un_tip_dat(cheltuieli, tip_dat) == 439.1

    tip_dat = "altele"
    assert suma_totala_pe_un_tip_dat(cheltuieli, tip_dat) == 0

    tip_dat = "mncare"
    try:
        suma_totala_pe_un_tip_dat(cheltuieli, tip_dat)
        assert False
    except ValueError as ve:
        assert str(ve) == "tip invalid!\n"

    assert ziua_suma_cheltuita_maxima(cheltuieli) == [20]

    zi = 21
    suma = 401.1
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    assert ziua_suma_cheltuita_maxima(cheltuieli) == [21]

    zi = 20
    suma = 256.6
    tip = "altele"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    assert ziua_suma_cheltuita_maxima(cheltuieli) == [20,21]

    zi = 23
    suma = 401.1
    tip = "altele"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    suma_data = 401.1

    assert cheltuielile_cu_suma_data(cheltuieli, suma_data) == [5, 7]

    suma_data = 66.3
    assert cheltuielile_cu_suma_data(cheltuieli, suma_data) == [3]

    suma_data = 1.3
    assert cheltuielile_cu_suma_data(cheltuieli, suma_data) == []

    suma_data = 0
    try:
        cheltuielile_cu_suma_data(cheltuieli, suma_data)
        assert False
    except ValueError as ve:
        assert str(ve) == "suma invalida!\n"


    assert cheltuieli_sortate_dupa_tip(cheltuieli) == [1, 3, 4, 0, 2, 5, 6, 7]

def ruleaza_teste_filtrari_cheltuiala():

    cheltuieli = []
    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    zi = 26
    suma = 17.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    tip_dat  = "altele"
    assert elimina_cheltuieli_tip_dat(cheltuieli, tip_dat) == [0, 1, 2, 3, 4]

    tip_dat = "mancare"
    assert elimina_cheltuieli_tip_dat(cheltuieli, tip_dat) == [0, 2]

    tip_dat = "twlefon"

    try:
        elimina_cheltuieli_tip_dat(cheltuieli, tip_dat)
        assert False
    except ValueError as ve:
        assert str(ve) == "tip invalid!\n"

    suma_data = 9.9
    assert elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data) == [0, 1 , 2, 3, 4]

    suma_data = 100.0
    assert elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data) == [0, 1]

    suma_data = 1000.0
    assert elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data) == []

    suma_data = -23.4
    try:
        elimina_cheltuieli_mai_mici_suma_data(cheltuieli, suma_data)
        assert False
    except ValueError as ve:
        assert str(ve) == "suma invalida!\n"

def ruleaza_teste_undo():
    cheltuieli = []
    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    nume_op = "stergere"
    zi_op = zi
    suma_op = suma
    tip_op = "intretinere"
    ind_op = 0

    operatie = creeaza_operatie(nume_op, zi_op, suma_op, tip_op, ind_op)

    assert get_nume_operatie(operatie) == nume_op
    assert get_zi_operatie(operatie) == zi_op
    assert get_suma_operatie(operatie) == suma_op
    assert get_tip_operatie(operatie) == tip_op
    assert get_indice_operatie(operatie) == 0

    operatii = []
    assert numar_operatii_lista(operatii) == 0

    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 1

    assert undo_adaugare(cheltuieli, operatii) == []
    assert numar_operatii_lista(operatii) == 0

    try:
        undo_adaugare(cheltuieli, operatii)
        assert False
    except ValueError as ve:
        assert str(ve) == "lista goala!\n"

    cheltuieli = []

    try:
        undo_actualizare(cheltuieli, operatii)
        assert False
    except ValueError as ve:
        assert str(ve) == "lista goala!\n"

    zi = 20
    suma = 500.0
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    nume_operatie = "stergere"
    ind_op = 0
    operatie = creeaza_operatie(nume_operatie, zi, suma, tip, ind_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 1


    zi_noua = 21
    suma_noua = 600.0
    tip_nou = "imbracaminte"
    set_zi_noua(cheltuieli[0], zi_noua)
    set_suma_noua(cheltuieli[0], suma_noua)
    set_tip_nou(cheltuieli[0], tip_nou)

    operatie = creeaza_operatie("actualizare", zi, suma, tip, 0)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 2

    cheltuieli = undo_actualizare(cheltuieli, operatii)
    assert cheltuieli == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}]
    assert numar_operatii_lista(operatii) == 1

    zi = 21
    suma = 355.5
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    operatie = creeaza_operatie("stergere", zi, suma, tip, 1)
    adauga_operatie_in_undo(operatii, operatie)

    assert numar_operatii_lista(operatii) == 2

    sterge_cheltuieli_zi_data(cheltuieli, 21)
    operatie = creeaza_operatie("adaugare", zi, suma, tip, 1)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 3

    assert undo_stergere(cheltuieli, operatii) == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua':21, 'suma': 355.5, 'tip': 'mancare'}]
    assert numar_operatii_lista(operatii) == 2

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    nume_op = "stergere"
    indice_op = 2
    operatie = creeaza_operatie(nume_op, zi, suma, tip, indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 3

    assert undo_complet(cheltuieli, operatii) == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua':21, 'suma': 355.5, 'tip': 'mancare'}]
    assert numar_operatii_lista(operatii) == 2

    zi = 3
    suma = 79.9
    tip = "imbracaminte"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    nume_op = "stergere"
    indice_op = 2
    operatie = creeaza_operatie(nume_op, zi, suma, tip, indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 3

    zi_noua = 4
    suma_noua = 80.1
    tip_nou = "telefon"
    set_zi_noua(cheltuieli[2], zi_noua)
    set_suma_noua(cheltuieli[2], suma_noua)
    set_tip_nou(cheltuieli[2], tip_nou)

    nume_op = "actualizare"
    indice_op = 2
    operatie = creeaza_operatie(nume_op, zi, suma, tip, indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 4

    cheltuieli = undo_complet(cheltuieli, operatii)
    assert cheltuieli == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua':21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]
    assert numar_operatii_lista(operatii) == 3

    sterge_cheltuieli_tip_dat(cheltuieli, "mancare")
    assert cheltuieli == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]

    nume_op = "adaugare"
    indice_op = 1
    operatie = creeaza_operatie(nume_op, 21, 355.5, "mancare", indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 4

    assert undo_complet(cheltuieli, operatii) == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua':21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]
    assert numar_operatii_lista(operatii) == 3

    zi = 23
    suma = 66.3
    tip = "mancare"
    cheltuiala = creeaza_cheltuiala(zi, suma, tip)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)

    nume_op = "stergere"
    indice_op = 3
    operatie = creeaza_operatie(nume_op, zi, suma, tip, indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 4

    sterge_cheltuieli_tip_dat(cheltuieli, "mancare")
    assert cheltuieli == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}]

    nume_op = "adaugare"
    indice_op = 1
    operatie = creeaza_operatie(nume_op, 21, 355.5, "mancare", indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 5

    nume_op = "adaugare"
    indice_op = 3
    operatie = creeaza_operatie(nume_op, 23, 66.3, "mancare", indice_op)
    adauga_operatie_in_undo(operatii, operatie)
    assert numar_operatii_lista(operatii) == 6

    undo_complet(cheltuieli, operatii)
    undo_complet(cheltuieli, operatii)

    assert cheltuieli == [{'ziua': 20, 'suma': 500.0, 'tip': 'intretinere'}, {'ziua':21, 'suma': 355.5, 'tip': 'mancare'}, {'ziua': 3, 'suma': 79.9, 'tip': 'imbracaminte'}, {'ziua': 23, 'suma': 66.3, 'tip': "mancare"}]
    assert numar_operatii_lista(operatii) == 4


def ruleaza_toate_testele():
    ruleaza_teste_cheltuiala()
    print("Teste cheltuiala rulate cu succes!")
    ruleaza_teste_validator_cheltuiala()
    print("Teste validator_cheltuiala rulate cu succes!")
    ruleaza_teste_repository_cheltuiala()
    print("Teste repository_cheltuiala rulate cu succes!")
    ruleaza_teste_cautari_cheltuiala()
    print("Teste cautari cheltuiala rulate cu succes!")
    ruleaza_teste_rapoarte_cheltuiala()
    print("Teste rapoarte_cheltuiala rulate cu succes!")
    ruleaza_teste_filtrari_cheltuiala()
    print("Teste filtrari_cheltuiala rulate cu succes!")
    ruleaza_teste_undo()
    print("Teste undo rulate cu succes!")