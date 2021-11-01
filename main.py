from Logic.CRUD import adauga_vanzare
from Tests.test_all import run_all_tests
from UI.consola import run_meniu


def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 100.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)
    run_meniu(lista)


main()
