import model

def izpis_igre(igra):
    return (
        f"Pravilni del gesla: {igra.pravilni_del_gesla()}\n" #f namesto .format()
        f"Neuspeli poskusi: {igra.nepravilni_ugibi()}\n"
        f"Število preostavlih poskusov: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n"
    )

def izpis_zmage(igra):
    return (
        "Čestitam, uganil si geslo\n"
        "Uspelo ti je v {} poskusih\n".format(len(igra.crke))
    )

def izpis_poraza(igra):
    return (
        "Porabil si vse poskuse\n"
        "Geslo je {}\n".format(igra.geslo)
    )

def zahtevaj_vnos():
    return input("Vnesi črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.ugibaj(poskus)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()