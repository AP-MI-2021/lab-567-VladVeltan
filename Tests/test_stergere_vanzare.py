from Logic.CRUD import adauga_vanzare, sterge_vanzare, get_by_id


def test_stergere():
    lista=[]
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100, "None", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 100, "None", lista)
    lista=sterge_vanzare("1",lista)
    assert len(lista)==1
    assert get_by_id("1",lista)is None
    assert get_by_id("2",lista) is not None
