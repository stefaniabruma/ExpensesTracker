

def creeaza_cheltuiala(zi, suma, tip):
    '''
    creeaza o cheltuiala cu ziua int zi, suma float suma, tipul string tip
    :param zi: int
    :param suma: float
    :param tip: string
    :return: cheltuiala cheltuiala cu ziua int zi, suma float suma si tipul string tip
    '''

    return{
        "ziua" : zi,
        "suma" : suma,
        "tip" : tip
    }

def get_zi_cheltuiala(cheltuiala):
    '''
    obtine ziua int a cheltuielii cheltuiala
    :param cheltuiala: cheltuiala
    :return: int - ziua cheltuielii cheltuiala
    '''
    return cheltuiala["ziua"]

def get_suma_cheltuiala(cheltuiala):
    '''
    obtine suma float a cheltuielii cheltuiala
    :param cheltuiala: cheltuiala
    :return: float - suma cheltuielii cheltuiala
    '''
    return cheltuiala["suma"]

def get_tip_cheltuiala(cheltuiala):
    '''
    obtine tipul string al cheltuielii cheltuiala
    :param cheltuiala: cheltuiala
    :return: string - tipul cheltuielii cheltuiala
    '''
    return cheltuiala["tip"]



