from Domain.vanzare import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modificare_vanzare


def print_meniu():
    print("1.Adaugare vanzare")
    print("2.Stergere vanzare")
    print("3.Modificare vanzare")
    print("a.Afisarea tuturor vanzarilor")
    print("x.Iesire")


def ui_adaugare_vanzare(lista):
    id = input("Dati id-ul:")
    titlu = input("Dati titlul:")
    gen_carte = input("Dati genul cartii:")
    pret = float(input("Dati pretul cartii:"))
    tip_reducere = input("Dati tipul de reducere al cartii:")
    return adauga_vanzare(id, titlu, gen_carte, pret, tip_reducere, lista)


def ui_stergere_vanzare(lista):
    id = input("Introduceti id-ul vanzarii care doriti sa fie sters: ")
    return sterge_vanzare(id, lista)


def ui_modificare_vanzare(lista):
    id = input("Dati id-ul de modificat:")
    titlu = input("Dati titlul de modificat:")
    gen_carte = input("Dati genul cartii de modificat:")
    pret = float(input("Dati pretul cartii de modificat:"))
    tip_reducere = input("Dati tipul de reducere al cartii de modificat:")
    return modificare_vanzare(id, titlu, gen_carte, pret, tip_reducere, lista)


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def run_meniu(lista):
    while True:
        print_meniu()
        optiune = input("Alegeti optiunea dorita: ")

        if optiune == "1":
            lista = ui_adaugare_vanzare(lista)

        elif optiune == "2":
            lista = ui_stergere_vanzare(lista)

        elif optiune == "3":
            lista = ui_modificare_vanzare(lista)

        elif optiune == "a":
            show_all(lista)

        elif optiune == "x":
            break
        else:
            print("Optiunea introdusa nu exista, reincercati: ")
