from Tests.test_adaugare_vanzare import test_adaugare
from Tests.test_domeniu import test_domeniu
from Tests.test_functionalitati import test_aplicare_reduceri, test_modificare_gen_dupa_titlu, test_pret_minim_dupa_gen, \
    test_ordonare_crescatoare_dupa_pret, test_afisare_nr_titluri_distincte_dupa_gen
from Tests.test_get_by_id import test_get_by_id
from Tests.test_modificare_vanzare import test_modificare
from Tests.test_stergere_vanzare import test_stergere


def run_all_tests():
    test_domeniu()
    test_adaugare()
    test_stergere()
    test_modificare()
    test_get_by_id()
    test_aplicare_reduceri()
    test_modificare_gen_dupa_titlu()
    test_pret_minim_dupa_gen()
    test_ordonare_crescatoare_dupa_pret()
    test_afisare_nr_titluri_distincte_dupa_gen()