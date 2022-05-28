'''
Die Implementierung entspricht der Bearbeitung einer Aufgabe aus:
Langtangen, Hans Petter(2016): A Primer on Scientific Programming with Python,
(= Texts in Computational Science and Engineering, Bd. 6),
Springer: Berlin / Heidelberg, 5. Auflage.

Simuliert wird die Entwicklung eines Vermögens x im Verlauf von n Jahren.

Vom Vermögen geht jedes Jahr ein Betrag zur Lebenshaltung ab, andererseits kommen Zinsen dazu:
x_n = x_n-1 + p/100*x_n-1 - c_n-1
Dabei ist x_n das Vermögen nach n Jahren, x_n-1 das Vermögen im Jahr davor, c_n-1 der Verbrauch im Jahr davor und p der Jahreszinssatz in Prozent.

Der Verbrauch steigt jedes Jahr durch die Inflation:
c_n = c_n-1 + I/100*c_n-1
I ist die Inflationsrate in Prozent, die den Verbrauch steigen lässt.

Der Startwert für das Vermögen ist FORTUNE, der Startwert für den Verbrauch ist q/100 * p/100 * FORTUNE, entspricht also q Prozent der Zinsen im ersten Jahr.

Es wird eine Text-Datei erzeugt, die für jedes Jahr den berechneten Vermögenswert und die berechneten Ausgaben auflistet.
'''

def living_from_fortune(initial_fortune, consume_from_initial, inflation_loss, interest_gain):
    # Umrechnung von Prozent auf Dezimal
    interest = interest_gain/100
    consume = consume_from_initial/100
    inflation = inflation_loss/100
    # Anfangsverbrauch
    consume_prev = interest*consume*initial_fortune
    # Anfangsvermögen
    fortune_prev = initial_fortune
    # Anfangsjahr
    year = 0
    # Simulation
    while fortune_prev >= 0 and year <= 50:
        # Vermögen plus Zinsen minus Verbrauch
        fortune = fortune_prev + interest*fortune_prev - consume_prev
        # nächster Verbrauch wächst um Inflation
        consume_prev += inflation*consume_prev
        # Vorbereitung der nächsten Runde
        fortune_prev = fortune
        year += 1
        # Ausgabe
        yield year, fortune, consume_prev

def main():
    # Anfangsvermögen
    FORTUNE = int(input('Geben Sie das Anfangsvermögen an: '))
    # Prozent der Zinsen vom ersten Jahr, die man verbraucht
    CONSUME_PERCENT = int(input('Wie viel Prozent der Zinsen im ersten Jahr geben Sie jährlich aus? '))
    # jährliche Inflation
    INFLATON_PERCENT = int(input('Wie groß ist die Inflation (Prozent)? '))
    # jährliche Zinsen aufs Vermögen
    INTEREST_PERCENT = int(input('Wie viele Zinsen erhalten Sie jährlich auf das Vermögen (Prozent)? '))
    # Datei erzeugen
    with open('fortune.txt', 'w', encoding='UTF-8') as outfile:
        outfile.write(f"Jahr {0:>3d}: fortune: {FORTUNE:>10.2f}, consume: {FORTUNE*CONSUME_PERCENT/100*INTEREST_PERCENT/100:>7.2f}\n")
        for year, fortune, consume in living_from_fortune(FORTUNE, CONSUME_PERCENT, INFLATON_PERCENT, INTEREST_PERCENT):
            outfile.write(f"Jahr {year:>3d}: fortune: {fortune:>10.2f}, consume: {consume:>7.2f}\n")
            
if __name__ == '__main__':
    main()