from Domain.vanzare import creeaza_vanzare, get_id, get_titlu


def adauga_vanzare(id, titlu, gen_carte, pret, tip_reducere, lista):
    """
    adauga o vanzare intr o lista
    :param id:id-ul cartii vandute-int
    :param titlu:titlul cartii-string
    :param gen_carte:genul cartii-string
    :param pret:pretul cartii-float
    :param tip_reducere:tipul de reducere aplicat-string
    :param lista: o lista care retine vanzarile
    :return: returneaza o lista continand lista veche plus vanzarea adaugata
    """
    if get_by_id(id,lista) is not None:
        raise ValueError("Id-ul introdus exista deja!")
    vanzare = creeaza_vanzare(id, titlu, gen_carte, pret, tip_reducere)
    return lista + [vanzare]


def get_by_id(id, lista):  # cautam in lista vanzarea care are id-ul introdus
    """
    cauta in lista vanzarea cu id-ul introdus
    :param id: id-ul dupa care se cauta vanzarea
    :param lista:lista de vanzari
    :return:vanzarea cu id-ul introdus, daca exista
    """
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None

def get_by_titlu(titlu,lista):
    """
    cauta in lista vanzare cu titlul-introdus
    :param titlu: titlul dupa care se cauta vanzarea
    :param lista: lista de vcanzari
    :return: vanzarea cu titlul-ul introdus, daca exista
    """
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            return vanzare
    return None

def sterge_vanzare(id, lista):
    """
    sterge o vanzare dupa id
    :param id: id-ul dupa care se executa stergerea
    :param lista:lista de vanzari
    :return:lista initiala fara vanzarea stearsa
    """
    if get_by_id(id,lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) != id:
            lista_noua.append(vanzare)
    return lista_noua


def modificare_vanzare(id, titlu, gen_carte, pret, tip_reducere, lista):
    """
    modifica o vanzare din lista curenta
    :param id:
    :param titlu:
    :param gen_carte:
    :param pret:
    :param tip_reducere:
    :param lista:lista ce contine vanzarile
    :return:returneaza o lista contind vanzarea dorita modificata
    """
    if get_by_id(id,lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id: #getid ia id-ul vanzarii pe care o parcurgem in lista , iar id este introdus de la tastatura
            vanzare_noua = creeaza_vanzare(id, titlu, gen_carte, pret, tip_reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua
