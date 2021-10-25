from Domain.vanzare import get_id, get_gen_carte, get_titlu, get_pret, get_tip_reducere
from Logic.CRUD import adauga_vanzare, modificare_vanzare, get_by_id


def test_modificare():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100, "None", lista)
    lista = adauga_vanzare("2", "Fat-Frumos", "fantastica", 100, "None", lista)

    lista = modificare_vanzare("1", "Cenusareasa", "Fantezie", 50, "None", lista)
    vanzare_updatata=get_by_id("1",lista)
    assert get_id(vanzare_updatata) == "1"
    assert get_titlu(vanzare_updatata) == "Cenusareasa"
    assert get_gen_carte(vanzare_updatata) == "Fantezie"
    assert get_pret(vanzare_updatata) == 50
    assert get_tip_reducere(vanzare_updatata) == "None"

    vanzare_neupdatata=get_by_id("2",lista)
    assert get_id(vanzare_neupdatata) == "2"
    assert get_titlu(vanzare_neupdatata) == "Fat-Frumos"
    assert get_gen_carte(vanzare_neupdatata) == "fantastica"
    assert get_pret(vanzare_neupdatata) == 100
    assert get_tip_reducere(vanzare_neupdatata) == "None"