from Domain.vanzare import get_id, get_titlu, get_gen_carte, get_pret, get_tip_reducere
from Logic.CRUD import adauga_vanzare, get_by_id


def test_get_by_id():
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100, "None", [])
    assert len(lista) == 1
    assert get_id(get_by_id("1",lista)) == "1"
    assert get_titlu(get_by_id("1",lista)) == "Harap Alb"
    assert get_gen_carte(get_by_id("1",lista)) == "fantastica"
    assert get_pret(get_by_id("1",lista)) == 100
    assert get_tip_reducere(get_by_id("1",lista)) == "None"
    lista = adauga_vanzare("2", "Fat-Frumos", "fantastica", 200, "None", lista)
    assert len(lista) == 2
    assert get_id(get_by_id("2", lista)) == "2"
    assert get_titlu(get_by_id("2", lista)) == "Fat-Frumos"
    assert get_gen_carte(get_by_id("2", lista)) == "fantastica"
    assert get_pret(get_by_id("2", lista)) == 200
    assert get_tip_reducere(get_by_id("2", lista)) == "None"