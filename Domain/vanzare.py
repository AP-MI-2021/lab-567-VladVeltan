def creeaza_vanzare(id, titlu, gen_carte, pret, tip_reducere):
    """
    creaza un dictionar pentru o vanzare
    :param id: id-ul cartii vandute-string
    :param titlu: titlul cartii-string
    :param gen_carte: genul cartii-string
    :param pret:pretul cartii-float
    :param tip_reducere:tipul de reducere aplicat-string
    :return: un dictonar care retine o vanzare
    """
    return {
        "id": id,
        "titlu": titlu,
        "gen_carte": gen_carte,
        "pret": pret,
        "tip_reducere": tip_reducere

    }


def get_id(vanzare):
    """
    da id-ul unei vanzari
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza id-ul unei carti vandute
    """
    return vanzare["id"]


def get_titlu(vanzare):
    """
    da titlul unei vanzari
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza titlul unei carti vandute
    """
    return vanzare["titlu"]


def get_gen_carte(vanzare):
    """
    da genul de carte
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza genul de carte
    """
    return vanzare["gen_carte"]


def get_pret(vanzare):
    """
    da pretul de vanzare al unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza pretul de vanzare al unei carti
    """
    return vanzare["pret"]


def get_tip_reducere(vanzare):
    """
    da tipul de reducere al unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: returneaza tipul de reducere al unei carti
    """
    return vanzare["tip_reducere"]

def to_string(vanzare):
    return "id: {}, titlu: {}, gen_carte: {}, pret: {}, tip_reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen_carte(vanzare),
        get_pret(vanzare),
        get_tip_reducere(vanzare)
    )

