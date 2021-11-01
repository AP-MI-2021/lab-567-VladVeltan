from Domain.vanzare import get_tip_reducere, creeaza_vanzare, get_id, get_titlu, get_gen_carte, get_pret


def aplicare_reduceri(lista):
    lista_noua = []
    for vanzare in lista:
        if get_tip_reducere(vanzare) == "silver":
            pret_modificat = get_pret(vanzare) - (get_pret(vanzare) * 5) / 100
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen_carte(vanzare),
                pret_modificat,
                get_tip_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        elif get_tip_reducere(vanzare) == "gold":
            pret_modificat = get_pret(vanzare) - (get_pret(vanzare) * 10) / 100
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen_carte(vanzare),
                pret_modificat,
                get_tip_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua


def modificare_gen_dupa_titlu(titlu, gen_modificat, lista):
    lista_noua = []
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            print("am ajuns la Harap Alb")
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_modificat,
                get_pret(vanzare),
                get_tip_reducere(vanzare)
            )
            print(get_gen_carte(vanzare_noua))
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua
