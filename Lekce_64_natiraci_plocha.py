
import math

# načteme hodnoty od uživatele
vyska_zdi = input("Zadej výšku zdi v metrech:\n")
sirka_zdi = input("Zadej šířku zdi v metrech:\n")
pokryti = 5

# vypočet plochy zdi - bez použití funkce
# vypocet_plochy = int(vyska_zdi) * int(sirka_zdi)
# print(vypocet_plochy)

# vypočet plochy zdi s pouzitím funkce
def calculator(vyska, sirka, plechovky):
    # jak velká je stěna (m2)
    plocha = int(vyska) * int(sirka)
    pocet_plechovek = plocha / pokryti
    # zaokrouhlení výpočetu
    pocet_plechovek = math.ceil(plocha / pokryti)
    print(pocet_plechovek)

calculator(vyska=vyska_zdi, sirka=sirka_zdi, plechovky=pokryti)