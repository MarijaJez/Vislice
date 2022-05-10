import bottle, model

vislice = model.Vislice()

@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/igra/")
def nova_igra():
    i = vislice.nova_igra()
    return bottle.redirect(f"/igra/{i}/")

@bottle.get("/igra/<id_igre:int>/") #ker smo definirali argument, ga lahko uporabimo v funkciji
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    geslo = igra.pravilni_del_gesla()
    nepravilni = igra.nepravilni_ugibi()
    obesenost = igra.stevilo_napak()
    celo_geslo = igra.geslo

    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'geslo': geslo, 'nepravilni': nepravilni, 'obesenost': obesenost, 'celo_geslo': celo_geslo})

@bottle.post("/igra/<id_igre:int>/")
def ugibaj(id_igre):
    crka = bottle.request.forms.crka
    if len(crka) == 1 and crka.isalpha():
        vislice.ugibaj(id_igre, crka)
    return bottle.redirect(f"/igra/{id_igre}/")

@bottle.get("/img/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True) #reloader=True: ob vsaki spremembi se na novo naloži

