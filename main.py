
from prezentare.ui import us_in
from testare.teste import ruleaza_toate_testele


def main():
    ruleaza_toate_testele()
    cheltuieli = []
    operatii = []
    nr_stergeri = []
    print("BINE ATI REVENIT")
    while True:
        us_in(cheltuieli, operatii, nr_stergeri)

main()