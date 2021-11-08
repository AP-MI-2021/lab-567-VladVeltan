from Logic.CRUD import adauga_vanzare
from Tests.test_all import run_all_tests
from UI.consola import run_meniu


def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)
    lista = adauga_vanzare("4", "Povestea micii sirene", "apa", 240.5, "silver", lista)
    lista = adauga_vanzare("5", "Fat Frumos din lacrima", "wow", 150.0, "gold", lista)

    run_meniu(lista)


main()
