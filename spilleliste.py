# Brukte 4 timer på denne filen. 
# Det var greit å følge tutorial i forelesning 10 med trikkestoppene og lage en lenket liste, men 
# da jeg skulle lage en linket liste med en klasse Sang inni klassen, ble det vanskelig å holde styr på hvordan jeg skulle gjøre det. 
# Klasse-ception. 

import logging
from sang import Sang

class SpillelisteKlasse:
    # Lenket liste er en objekttype jeg ikke har vært borti tidligere. :) Nyttig og spennende datatype. 
    def __init__(self, data):
        self._forrige = None
        self._data = data
        self._neste = None

    def __str__(self) -> str:
        # Spol tilbake til den første sangen. 
        while self._forrige != None:
            self = self._forrige 
        # List opp alle sangene. 
        streng = ''
        while self._neste != None:
            streng += f'{self._data} \n'
            self = self._neste
        streng += f'{self._data} \n'
        return streng

    def append(self, tittel, artist):
        while self._neste != None:
            self = self._neste

        DenneSangen = Sang(tittel, artist)
        DenneSangenISpillelisten = SpillelisteKlasse(DenneSangen)
        self._neste = DenneSangenISpillelisten
        DenneSangenISpillelisten.ForrigeSang(self)

    def pop(self):
        while self._neste != None:
            self = self._neste
        siste = self
        self = self._forrige
        self._neste = None
        siste._forrige = None
        return self

    def SpolForover(self):
        self = self._neste
    
    def SpolBakover(self):
        # self = self._forrige
        return self._forrige

    def NesteSang(self, NesteSang):
        self._neste = NesteSang    

    def ForrigeSang(self, ForrigeSang):
        self._forrige = ForrigeSang  

    def HentNavn(self):
        return str(self._data)

def LesFraFil(filnavn):
    DenneSangenISpillelisten = None
    with open(filnavn) as f:
        for linje in f:
            DenneSangen = linje.strip().split(';')
            DenneSangen = Sang(DenneSangen[0], DenneSangen[1])

            if DenneSangenISpillelisten:
                DenneSangenISpillelisten = SpillelisteKlasse(DenneSangen)
                # Fortelle den forje sangen i spillelisten hva som er DenneSangenISpillelisten: 
                ForjeSangenISpillelisten.NesteSang(DenneSangenISpillelisten)
                DenneSangenISpillelisten.ForrigeSang(ForjeSangenISpillelisten)
                ForjeSangenISpillelisten = DenneSangenISpillelisten
            else:
                # Legg inn første sang: 
                DenneSangenISpillelisten = SpillelisteKlasse(DenneSangen)
                ForjeSangenISpillelisten = DenneSangenISpillelisten
            # Midlertidig huske hva som var den forje sangen i neste iterasjon. 
    # Denne return statementen skapte problemer fordi den siste sangen hadde ikke referanse til de forann seg, så jeg måtte lege til
    # self._forrige slik at jeg kunne spole bakover i den linkede listen. Dermed ble dette en dobbelt-linket liste? 
    return DenneSangenISpillelisten

def main():
    Liste1 = LesFraFil("C:\\VisualStudioCode\\IN1000\\OBLIG7\\sang_liste.txt")
    Liste1.append('Chase', 'Giorgio Moroder')
    # print(Liste1)
    Liste1 = Liste1.SpolForover()
    print(f'Peke mot siste gjenstand i liste: {Liste1.HentNavn()}') 
    Liste1.pop()

    # Liste1 = Liste1.pop()
    print(Liste1)

    print(Liste1.HentNavn()) 

    # Denne funksjonen fungerer ikke. Jeg får ikke til å spole fremover eller bakover i listen. 
    ForrigeSang = Liste1.SpolBakover()
    print(ForrigeSang.HentNavn()) 

if __name__=='__main__':
    main()