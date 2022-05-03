import model

SLIKE = [    
    '',
"""




___---_""",
"""
 | 
 |
 |
 | 
_|__---_""",
""" _____
 |   
 |   
 |  
 |  
_|__---_""",
""" _____
 |   |
 |  
 |  
 |  
_|__---_""",
""" _____
 |   |
 |   o
 |  
 |  
_|__---_""",
""" _____
 |   |
 |   o
 |   |
 |  
_|__---_""",
""" _____
 |   |
 |   o
 |  /|
 |  
_|__---_""",
""" _____
 |   |
 |   o
 |  /|\\
 |   
_|__---_""",
""" _____
 |   |
 |   o
 |  /|\\
 |  / 
_|__---_""",
""" _____
 |   |
 |   o
 |  /|\\
 |  / \\
_|__---__""",
""" _____
 |   |
 |   o
 |  /|\\
 |  / \\
_|_______"""]
def izpis_igre(igra):
    niz = f"""{SLIKE[igra.stevilo_napak()]} 
    {igra.pravilni_del_gesla()}
    Nepravilni ugibi: {igra.nepravilni_ugibi()}
    Dovoljenih napačnih ugibov še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}"""
    return niz

def izpis_zmage(igra):
    niz = f"Čestitke! Pravilno ste uganili geslo {igra.geslo}."
    return niz

def izpis_poraza(igra):
    niz = f"Več sreče prihodnjič. Geslo je bilo {igra.geslo}."
    return niz

def zahtevaj_vnos():
    return input("Ugibaj črko: ")



def pozeni_vmesnik():
    igra = model.nova_igra()
    while not igra.zmaga() and not igra.poraz():
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        while len(crka) != 1 or not crka.isalpha():
            crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))
    else:
        print(SLIKE[-1])
        print(izpis_poraza(igra))
    
    odlocitev = input("Bi želeli igrati ponovno? (D/N): ")
    if odlocitev == 'D':
        pozeni_vmesnik()

pozeni_vmesnik()