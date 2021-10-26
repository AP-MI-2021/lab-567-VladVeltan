def creeaza_vanzare(id, titlu, gen_carte, pret, tip_reducere):
    """
    creaza o lista de tupluri pentru o vanzare
    :param id: id-ul cartii vandute-string
    :param titlu: titlul cartii-string
    :param gen_carte: genul cartii-string
    :param pret:pretul cartii-float
    :param tip_reducere:tipul de reducere aplicat-string
    :return: o lista de tupluri care retine o vanzare
    """

    return (
        id,
        titlu,
        gen_carte,
        pret,
        tip_reducere
    )


def get_id(vanzare):
    """
    da id-ul unei vanzari
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza id-ul unei carti vandute
    """
    return vanzare[0]


def get_titlu(vanzare):
    """
    da titlul unei vanzari
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza titlul unei carti vandute
    """
    return vanzare[1]


def get_gen_carte(vanzare):
    """
    da genul de carte
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza genul de carte
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    da pretul de vanzare al unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza pretul de vanzare al unei carti
    """
    return vanzare[3]


def get_tip_reducere(vanzare):
    """
    da tipul de reducere al unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza tipul de reducere al unei carti
    """
    return vanzare[4]


def to_string(vanzare):
    return "id: {}, titlu: {}, gen_carte: {}, pret: {}, tip_reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen_carte(vanzare),
        get_pret(vanzare),
        get_tip_reducere(vanzare)
    )
