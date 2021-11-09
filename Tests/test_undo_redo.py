#from Logic.CRUD import adauga_vanzare
from UI.consola import ui_adaugare_vanzare


def test_undo_si_redo():
    lista=[]
    undo_list=[]
    redo_list=[]



    lista = ui_adaugare_vanzare(lista, undo_list, redo_list)
    lista = ui_adaugare_vanzare(lista, undo_list, redo_list)
    lista = ui_adaugare_vanzare(lista, undo_list, redo_list)

    assert len(lista)==3

    #lista = adauga_vanzare("4", "Povestea micii sirene", "apa", 240.5, "silver", lista)
    #lista = adauga_vanzare("5", "Fat Frumos din lacrima", "wow", 150.0, "gold", lista)
