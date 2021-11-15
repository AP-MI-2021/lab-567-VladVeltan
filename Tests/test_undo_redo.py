from Logic.CRUD import adauga_vanzare, get_by_id
from UI.consola import redoo, undoo


def test_undo_si_redo():
    # 1 lista goala
    lista = []
    undo_list = []
    redo_list = []
    # 2 adaugam un element
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)

    # 3 adaugam alt elemente
    undo_list.append(lista)  # apar inaintea functiilor de adaugare/stergere/modificare in def-urile din UI
    redo_list.clear()  # pentru a salva in lista rezultatele inainte de modificarea facuta
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)

    # 4 adaugam alt element
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    assert len(lista) == 3

    # 5 dam undo si dispare ultima adaugare

    lista = undoo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is not None
    assert get_by_id('3', lista) is None

    # 6 undo raman doar un element
    lista = undoo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None

    # 7 undo nu ramane nimic
    lista = undoo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id('1', lista) is None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None

    # 8 undo, nu face nimic

    assert len(lista) == 0
    assert get_by_id('1', lista) is None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None

    # 9 adaugam 3 elemente
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)

    undo_list.append(lista)  # apar inaintea functiilor de adaugare/stergere/modificare in def-urile din UI
    redo_list.clear()  # pentru a salva in lista vanzarile inainte de modificarea facuta
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)

    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    # 10 redo nu face nimic
    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is not None
    assert get_by_id('3', lista) is not None

    # 11 doua undo-uri , dispar ultimele doua vanzari
    lista = undoo(lista, undo_list, redo_list)
    lista = undoo(lista, undo_list, redo_list)

    assert len(lista) == 1
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None

    # 12 redo anuleaza ultimul undo, daca ultima operatie e undo

    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is not None
    assert get_by_id('3', lista) is None

    # 13 redo anuleaza si primul undo

    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is not None
    assert get_by_id('3', lista) is not None

    # 14 doua undo-uri scot ultimele 2 obiecte

    lista = undoo(lista, undo_list, redo_list)
    lista = undoo(lista, undo_list, redo_list)

    assert len(lista) == 1
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None

    # 15 adaugam un obiect
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_vanzare("4", "Povestea micii sirene", "apa", 240.5, "silver", lista)

    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is not None

    # 16 redo nu face nimic, deoarece ultima operatie nu este un undo
    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is not None

    # 17 undo anuleaza adaugarea lui o4
    lista = undoo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is None

    # 18 undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    lista = undoo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id('1', lista) is None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is None

    # 19 se anuleaza ultimele 2 undo-uri
    lista = redoo(lista, undo_list, redo_list)
    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is not None

    # 20 redo nu face nimic
    lista = redoo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id('1', lista) is not None
    assert get_by_id('2', lista) is None
    assert get_by_id('3', lista) is None
    assert get_by_id('4', lista) is not None
