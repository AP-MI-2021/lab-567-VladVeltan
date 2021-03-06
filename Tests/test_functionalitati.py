from Domain.vanzare import get_pret, get_gen_carte, get_id
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitati import aplicare_reduceri, modificare_gen_dupa_titlu, pret_minim_dupa_gen, \
    ordonare_crescatoare_dupa_pret, afisare_nr_titluri_distincte_dupa_gen


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


def test_pret_minim_dupa_gen():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    rezultat = pret_minim_dupa_gen(lista)

    assert len(rezultat) == 2
    assert rezultat["fantastica"] == 100.0
    assert rezultat["apa"] == 280.0


def test_ordonare_crescatoare_dupa_pret():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    rezultat = ordonare_crescatoare_dupa_pret(lista)

    assert get_id(rezultat[0]) == "2"
    assert get_id(rezultat[1]) == "3"
    assert get_id(rezultat[2]) == "1"


def test_afisare_nr_titluri_distincte_dupa_gen():
    lista = []
    lista = adauga_vanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)
    lista = adauga_vanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)
    lista = adauga_vanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)
    lista = adauga_vanzare("4", "Povestea micii sirene", "apa", 240.5, "silver", lista)
    lista = adauga_vanzare("5", "Fat Frumos din lacrima", "wow", 150.0, "gold", lista)

    rezultat=afisare_nr_titluri_distincte_dupa_gen(lista)

    assert len(rezultat)==3
    assert rezultat["apa"]==1 #cazul cand titlul si genul sunt egale
    assert rezultat["fantastica"]==2
    assert rezultat["wow"]==1



