from Logic.CRUD import adauga_vanzare
from Tests.test_all import run_all_tests
from UI.consola import run_meniu


def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100, "None", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 100, "None", lista)
    run_meniu(lista)


main()