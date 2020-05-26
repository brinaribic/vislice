import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 's'
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ ='X'

DATOTEKA = 'stanje.json'
BESEDE = 'besede.txt'
class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK
    
    def zmaga(self):
        #return set(self.geslo) == set(self.pravilne_crke())
        #return all(crka in self.crke in self.geslo)
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            s += crka if crka in self.crke else '_ '
        return s

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(ugibana_crka)
            if ugibana_crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []
for beseda in open(BESEDE, encoding='utf-8'):
    self.bazen_besed.append(beseda.strip().upper())

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)

class Vislice:
    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami):
        self.igre = {}
        self.bazen_besed = []
        for beseda in open(datoteka_z_besedami, encoding='utf-8'):
            self.bazen_besed.append(beseda.strip().upper())
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.nalozi_igre_iz_datoteke()

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = Igra(random.choice(self.bazen_besed))
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteke()
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre] #stanje = _ ker tega ne bomo nikoli uporabli
        stanje = igra.ugibaj(crka) #novo stanje
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteke()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, encoding='utf-8') as f:
            igre = json.load(f) #slovar, ki vsebuje podatke o vseh igrah
            self.igre = {int(id_igre): (Igra(geslo, crke), stanje)for id_igre, (geslo, crke, stanje) in igre.items()}

    def zapisi_igre_v_datoteke(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.geslo, igra.crke, stanje) for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f)

# self.igre = {0: (Igra(geslo, crke), stanje)}
# igre = {0: (geslo, crke, stanje)}


