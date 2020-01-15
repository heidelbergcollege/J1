class Buch:
    def __init__(self, pTitel, pAnzahlSeiten, pPreis):
        self.titel = pTitel
        self.anzahlSeiten = pAnzahlSeiten
        self.preis = pPreis

buecherliste = []
programmRunning = True

while programmRunning:
    aktion = input("Was möchten Sie tun? Buch [A]nlegen, Büchreliste [D]rucken, Buch [S]uchen oder Programm [B]eenden?").upper()

    if aktion == 'A':
        titel = input("Bitte geben Sie einen Buchtitel ein: ")
        anzahlSeiten = input("Bitte geben Sie die Seitenanzahl ein: ")
        preis = input("Bitte geben Sie den Preis ein: ")
        buch = Buch(titel, anzahlSeiten, preis)
        buecherliste.append(buch)
    elif aktion == 'D':
        continue
    elif aktion == 'S':
        continue
    elif aktion == 'B':
        programmRunning = False
