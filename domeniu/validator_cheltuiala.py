

def valideaza_cheltuiala(cheltuiala):
    '''
    verifica daca ziua int a cheltuielii cheltuiala este existenta
             daca suma float a chletuielii cheltuiala este strict pozitiva
             daca tipul string al cheltuielii cheltuiala sa afla in multimea {"mancare", "intretinere", "imbracaminte", "telefon", "altele"}
    daca cel putin un atribut al cheltuielii cheltuiala este invalid, arunca exceptie de tipul ValueError
    :param cheltuiala: cheltuiala
    :return: -
    :raises: ValueError daca datele din cheltuiala sunt invalide:
                        daca zi < 1 sau zi > 31  -> "zi invalida!\n"
                        daca suma <= 0 -> "suma invalida!\n"
                        daca tip != "mancare" and tip != "intretinere" and tip != "imbracaminte" and tip != "telefon" and tip != "altele" -> "tip invalid!\n"
    '''

    errors = ""
    if cheltuiala["ziua"] < 1 or cheltuiala["ziua"] > 31:
        errors += "zi invalida!\n"
    if cheltuiala["suma"] <= 0:
        errors += "suma invalida!\n"
    lista_posibilitati = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]
    ok = 0
    for i in lista_posibilitati:
        if cheltuiala["tip"] == i:
            ok = 1
    if ok == 0:
        errors += "tip invalid!\n"
    if len(errors) > 0:
        raise ValueError(errors)

