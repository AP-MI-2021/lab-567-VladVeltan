from Logic.CRUD import adauga_vanzare
from Domain.vanzare import get_id, get_titlu, get_gen_carte, get_pret, get_tip_reducere


def test_adaugare():
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100, "None", [])
    # aici verificam cate elem avem in lista
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert get_titlu(lista[0]) == "Harap Alb"
    assert get_gen_carte(lista[0]) == "fantastica"
    assert get_pret(lista[0]) == 100
    assert get_tip_reducere(lista[0]) == "None"
