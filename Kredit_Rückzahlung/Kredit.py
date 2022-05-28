'''
Die Implementierung entspricht der Bearbeitung einer Aufgabe aus:
Langtangen, Hans Petter(2016): A Primer on Scientific Programming with Python,
(= Texts in Computational Science and Engineering, Bd. 6),
Springer: Berlin / Heidelberg, 5. Auflage.

Simuliert wird die monatliche Rückzahlrate nach Aufnahme eines Kredites zu bestimmten Konditionen.

Der Kredit erhöht sich jeden Monat um die festgelegte Zinsrate, gleichzeitig wird der zurückgezahlte Betrag abgezogen.
Wenn die Monate mit n durchgezählt werden, die Rate des n-ten Monats y_n ist und der Kreditstand im n-ten Monat x_n beträgt, dann gilt:
y_n = p/12/100*x_n-1 + L/N
x_n = x_n-1 + p/12/100*x_n-1 - y_n
Hierbei ist p die jährlich Zinsrate, die auf die monatliche Zinsrate umgerechnet wird (p/12).
L ist die Höhe des ursprünglichen Kredits und N ist die Zahl der Monate, über die der Kredit abbezahlt werden soll.

Angegeben wird im Programm die Zahl der Jahre, die Umrechnung auf Monate erfolgt automatisch.
'''

def kreditrate(kredit, monate, zinsrate_jahr):
    rate = kredit/monate
    zinsrate_monat = zinsrate_jahr/(12*100)
    monat = 1
    letzter_kredit = kredit
    while monat <= monate:
        betrag_monat = zinsrate_monat*letzter_kredit + rate
        neuer_kredit = letzter_kredit + zinsrate_monat*letzter_kredit - betrag_monat
        letzter_kredit = neuer_kredit
        monat += 1
        yield monat-1, betrag_monat, neuer_kredit

def main():
    KREDIT = float(input('Wie hoch ist der Kredit? '))
    JAHRE = float(input("Über wie viele Jahre soll der Kredit abbezahlt werden? "))
    monate = 12*JAHRE
    ZINSRATE_JAHR = 2.5
    with open('kredit.txt', 'w', encoding='UTF-8') as outfile:
        outfile.write(f"Monat {0:>3d}: Rückzahlung: {0:>8.2f}, Kredit: {KREDIT:>8.2f}\n")
        for monat, betrag, kredit in kreditrate(KREDIT, monate, ZINSRATE_JAHR):
            outfile.write(f"Monat {monat:>3d}: Rückzahlung: {betrag:>8.2f}, Kredit: {kredit:>8.2f}\n")
            if monat % 12 == 0:
                outfile.write('\n')

if __name__ == '__main__':
    main()