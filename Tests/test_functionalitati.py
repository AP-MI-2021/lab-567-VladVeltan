from Domain.vanzare import get_pret, get_gen_carte
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitati import aplicare_reduceri, modificare_gen_dupa_titlu


def test_aplicare_reduceri():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 100.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    lista = aplicare_reduceri(lista)

    assert get_pret(get_by_id("1", lista)) == 95.0
    assert get_pret(get_by_id("2", lista)) == 90.0
    assert get_pret(get_by_id("3", lista)) == 280.0


def test_modificare_gen_dupa_titlu():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 100.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    titlu = "Harap Alb"
    gen_modificat = "poveste"
    lista = modificare_gen_dupa_titlu(titlu, gen_modificat, lista)


    assert get_gen_carte(get_by_id("1", lista)) == gen_modificat
    assert get_gen_carte(get_by_id("2", lista)) == "fantastica"

    titlu = "Povestea micii sirene"
    gen_modificat = "Poveste de dragoste"

    lista = modificare_gen_dupa_titlu(titlu, gen_modificat, lista)

    assert get_gen_carte(get_by_id("3", lista)) == gen_modificat
