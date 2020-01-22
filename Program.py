class Buch:
    def __init__(self, pTitel, pAnzahlSeiten, pPreis):
        self.titel = pTitel
        self.anzahlSeiten = pAnzahlSeiten
        self.preis = pPreis

buecherliste = []
programmRunning = True

while programmRunning:
    aktion = input("Was möchten Sie tun? Buch [A]nlegen, Bücherliste [D]rucken, Buch [S]uchen, Buch in [W]arenkorb, Zur [K]asse oder Programm [B]eenden?").upper()

    if aktion == 'A':
        titel = input("Bitte geben Sie einen Buchtitel ein: ")
        anzahlSeiten = input("Bitte geben Sie die Seitenanzahl ein: ")
        preis = input("Bitte geben Sie den Preis ein: ")
        buch = Buch(titel, anzahlSeiten, preis)
        buecherliste.append(buch)
    elif aktion == 'D':
        for buch in buecherliste:
            print(buch.titel, buch.anzahlSeiten, buch.preis)
    elif aktion == 'S':
        titel = input("Welchen Buchtitel suchen Sie? ")
        gefundenesBuch = ""
        buchGefunden = False
        for buch in buecherliste:
            if buch.titel == titel:
                gefundenesBuch = buch
                buchGefunden = True
            if buchGefunden == True:
                break
        if buchGefunden == True:
            print("Wir haben Ihr Buch:")
            print(gefundenesBuch.titel, gefundenesBuch.anzahlSeiten, gefundenesBuch.preis)
    elif aktion == 'W':
        continue
    elif aktion == 'K':
        continue
    elif aktion == 'B':
        programmRunning = False
