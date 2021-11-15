from Domain.vanzare import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modificare_vanzare
from Logic.functionalitati import aplicare_reduceri, modificare_gen_dupa_titlu, pret_minim_dupa_gen, \
    ordonare_crescatoare_dupa_pret, afisare_nr_titluri_distincte_dupa_gen


def print_meniu():
    print("1.Adaugare vanzare")
    print("2.Stergere vanzare")
    print("3.Modificare vanzare")
    print("4.Aplicare reduceri")
    print("5.Modificarea genului pentru un titlu dat")
    print("6.Determinarea prețului minim pentru fiecare gen")
    print("7.Ordonarea vânzărilor crescător după preț")
    print("8.Afișarea numărului de titluri distincte pentru fiecare gen")
    print("c.Schimba interfata")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisarea tuturor vanzarilor")
    print("x.Iesire")


def ui_adaugare_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul:")
        titlu = input("Dati titlul:")
        gen_carte = input("Dati genul cartii:")
        pret = float(input("Dati pretul cartii:"))
        tip_reducere = input("Dati tipul de reducere al cartii:")

        rezultat = adauga_vanzare(id, titlu, gen_carte, pret, tip_reducere,
                                  lista)
        # punem functia de adaugare in rezultat
        # pentru a evita o exceptie in cazul unei adaugari gresite
        undo_list.append(lista)  # pune in undo.list lista de inainte de adaugare
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Introduceti id-ul vanzarii care doriti sa fie sters: ")
        rezultat = sterge_vanzare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul de modificat:")
        titlu = input("Dati titlul de modificat:")
        gen_carte = input("Dati genul cartii de modificat:")
        pret = float(input("Dati pretul cartii de modificat:"))
        tip_reducere = input("Dati tipul de reducere al cartii de modificat:")
        rezultat = modificare_vanzare(id, titlu, gen_carte, pret, tip_reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_aplicare_reduceri(lista, undo_list, redo_list):
    rezultat = aplicare_reduceri(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_modificare_gen_dupa_titlu(lista, undo_list, redo_list):
    titlu = input("Introduceti titlul pentru care urmeaza a se efectua modificarea:")
    gen_modificat = input("Introduceti genul modificat:")
    rezultat = modificare_gen_dupa_titlu(titlu, gen_modificat, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_pret_minim_dupa_gen(lista):
    rezultat = pret_minim_dupa_gen(lista)
    for gen in rezultat:
        print("Pretul minim pentru genul {} este {}".format(gen, rezultat[gen]))  # rezultat[gen] e pretul cartii


def ui_ordonare_crescatoare_dupa_pret(lista):
    show_all(ordonare_crescatoare_dupa_pret(lista))


def ui_afisare_nr_titluri_distincte_dupa_gen(lista):
    rezultat = afisare_nr_titluri_distincte_dupa_gen(lista)
    for gen in rezultat:
        print("Pentru genul {} exista {} titluri distincte".format(gen, rezultat[gen]))


def print_meniu_clc():
    print("add.Adaugare vanzare")
    print("delete.Stergere vanzare")
    print("showall.Afisare vanzari")
    print("change.Schimba interfata")
    print("stop.Oprire program")


def run_meniu_cls(lista):
    print(print_meniu_clc())
    breaker = 1
    while True:
        comanda_liniara = input("Introduceti comenzi: ")
        comanda_liniara = comanda_liniara.split(';')
        for comanda in comanda_liniara:
            comanda = comanda.split(',')
            if comanda[0] == "add":
                if len(comanda) == 6:
                    try:
                        id = comanda[1]
                        titlu = comanda[2]
                        gen = comanda[3]
                        pret = float(comanda[4])
                        reducere = comanda[5]
                        lista = adauga_vanzare(id, titlu, gen, pret, reducere, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Eroare: Numar invalid de parametrii')
            elif comanda[0] == "showall":
                show_all(lista)
            elif comanda[0] == "delete":
                if len(comanda) == 2:
                    try:
                        id = comanda[1]
                        lista = sterge_vanzare(id, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print("Eroare: Numar invalid de parametrii")
            elif comanda[0] == "change":
                run_meniu_simplu(lista)
                breaker = 0
            elif comanda[0] == "stop":
                breaker = 0
                break
            else:
                print("Comanda gresita! Reincercati!")
        if breaker == 0:
            break


def run_meniu_simplu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_meniu()
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            lista = ui_adaugare_vanzare(lista, undo_list, redo_list)

        elif optiune == "2":
            lista = ui_stergere_vanzare(lista, undo_list, redo_list)

        elif optiune == "3":
            lista = ui_modificare_vanzare(lista, undo_list, redo_list)

        elif optiune == "4":
            lista = ui_aplicare_reduceri(lista, undo_list, redo_list)

        elif optiune == "5":
            lista = ui_modificare_gen_dupa_titlu(lista, undo_list, redo_list)

        elif optiune == "6":
            ui_pret_minim_dupa_gen(lista)

        elif optiune == "7":
            ui_ordonare_crescatoare_dupa_pret(lista)

        elif optiune == "8":
            ui_afisare_nr_titluri_distincte_dupa_gen(lista)
        elif optiune == "c":
            run_meniu_cls(lista)
            break
        elif optiune == "u":
            lista = undo(lista, undo_list, redo_list)
        elif optiune == "r":
            lista = redo(lista, undo_list, redo_list)
        elif optiune == "a":
            show_all(lista)

        elif optiune == "x":
            break
        else:
            print("Optiunea introdusa nu exista, reincercati: ")


def undo(lista, undo_list, redo_list): #intra mereu pe else
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()  # .pop() ia ultima valoare din lista
    else:
        print("Nu se poate face undo!")
    return lista

def undoo(lista, undo_list, redo_list): #intra mereu pe else
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()  # .pop() ia ultima valoare din lista
    return lista

def redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    else:
        print("Nu se poate face redo!")
    return lista
def redoo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    return lista

def run_meniu(lista):
    while True:
        print("1.Consola simpla")
        print("2.Consola liniara")
        print("x.Exit")
        optiune_meniu = input("Alegeti interfata dorita:")
        if optiune_meniu == "1":
            run_meniu_simplu(lista)
        elif optiune_meniu == "2":
            run_meniu_cls(lista)
        elif optiune_meniu == "x":
            break
        else:
            print("Optiunea introdusa nu exista,reincercati!")
