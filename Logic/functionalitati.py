from Domain.vanzare import get_tip_reducere, creeaza_vanzare, get_id, get_titlu, get_gen_carte, get_pret


def aplicare_reduceri(lista):
    """
    aplica reducerile pentru fiecare carte
    :param lista: lista cartilor
    :return: lista cartilor cu reducerile aplicate
    """
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


def modificare_gen_dupa_titlu(titlu, gen_modificat, lista):  # trb exceptie daca se introduce titlu care nu exista
    """
    modifica genul unei carti dupa titlul cautat
    :param titlu: titlul introdus de la tastatura
    :param gen_modificat: genul cartii modificat
    :param lista: lista de carti
    :return: lista cu genurile modificate dupa titlul introdus initial
    """
    lista_noua = []
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_modificat,
                get_pret(vanzare),
                get_tip_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua


def pret_minim_dupa_gen(lista):  # determina pretul minim pentru fiecare gen
    """
    returneaza un dictionar care contine pretul minim pentru fiecare gen din lista
    :param lista: lista de carti/vanzari
    :return: un dictionar care contine pretul minim pentru fiecare gen din lista
    """
    rezultat = {}
    for vanzare in lista:
        gen = get_gen_carte(vanzare)  # good practice cand apelam o functie de mai multe ori
        pret = get_pret(vanzare)
        if gen in rezultat:  # verifica daca e in dicitonar
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:  # daca nu e in dictionar il pune
            rezultat[gen] = pret
    return rezultat


def ordonare_crescatoare_dupa_pret(lista):
    """
    returneaza lista ordonata crescator dupa pret
    :param lista: lista de vanzari
    :return: returneaza lista ordonata crescator dupa pret
    """
    # lista.sort() sorteaza lista efectiv, noi dorim doar afisare ordonata
    return sorted(lista, key=lambda vanzare: get_pret(vanzare))


def afisare_nr_titluri_distincte_dupa_gen(lista):
    """
    returneaza numar de titluri distincte pentru fiecare gen
    :param lista: lista de carti
    :return: numar de titluri distincte pentru fiecare gen
    """
    rezultat = {}
    lista_titluri = []
    for vanzare in lista:
        gen = get_gen_carte(vanzare)
        titlu = get_titlu(vanzare)
        if gen in rezultat:
            if titlu not in lista_titluri:
                lista_titluri.append(titlu)
                rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1
            lista_titluri.append(titlu)
    return rezultat
