from Domain.vanzare import creeaza_vanzare, get_id, get_titlu, get_gen_carte, get_pret, get_tip_reducere


def test_domeniu():
    vanzare = creeaza_vanzare("1", "Harap Alb", "fantastica", 100, "None")
    assert get_id(vanzare) == "1"
    assert get_titlu(vanzare) == "Harap Alb"
    assert get_gen_carte(vanzare) == "fantastica"
    assert get_pret(vanzare) == 100
    assert get_tip_reducere(vanzare) == "None"
    # facem test la domeniu pentru a verifica eventuale erori cauzate de typo-uri

