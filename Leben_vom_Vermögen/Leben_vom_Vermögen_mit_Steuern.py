'''
Die Implementierung entspricht der Bearbeitung einer Aufgabe aus:
Langtangen, Hans Petter(2016): A Primer on Scientific Programming with Python,
(= Texts in Computational Science and Engineering, Bd. 6),
Springer: Berlin / Heidelberg, 5. Auflage.

Simuliert wird die Entwicklung eines Vermögens x im Verlauf von n Jahren.

Vom Vermögen geht jedes Jahr ein Betrag zur Lebenshaltung ab, andererseits kommen Zinsen dazu.
Hier werden Zinsen erst gutgeschrieben, nachdem über das Jahr verteilt Geld ausgegeben wurde.
Zusätzlich wird hier noch der Einfluss von Steuern auf den Gewinn berücksichtigt:
x_n = x_n-1 - c_n-1 + p/100*(x_n-1 - c_n-1) - t/100*(x_n-1 - x_n-2)
Dabei ist x_n das Vermögen nach n Jahren, x_n-1 das Vermögen im Jahr davor, c_n-1 der Verbrauch im Jahr davor und p der Jahreszinssatz in Prozent.
t ist der Steuersatz auf den Gewinn vom Vorjahr.

Der Verbrauch steigt jedes Jahr durch die Inflation:
c_n = c_n-1 + I/100*c_n-1
I ist die Inflationsrate in Prozent, die den Verbrauch steigen lässt.

Der Startwert für das Vermögen ist FORTUNE, der Startwert für den Verbrauch ist CONSUME.

Es wird eine Text-Datei erzeugt, die für jedes Jahr den berechneten Vermögenswert und die berechneten Ausgaben auflistet.
'''

def living_from_fortune(initial_fortune, consume_initial, inflation_loss, interest_gain, tax_loss):
    # Umrechnung von Prozent auf Dezimal
    interest = interest_gain/100
    inflation = inflation_loss/100
    tax = tax_loss/100
    # Anfangsverbrauch
    consume_prev = consume_initial
    # Anfangsvermögen
    fortune_prev = initial_fortune
    fortune_2prev = initial_fortune
    # Anfangsjahr
    year = 0
    # Simulation
    while fortune_prev >= 0 and year <= 100:
        gewinn = fortune_prev - fortune_2prev
        if gewinn > 0:
            fortune = fortune_prev - consume_prev + interest*(fortune_prev - consume_prev) - tax*(fortune_prev - fortune_2prev)
        else:
            fortune = fortune_prev - consume_prev + interest*(fortune_prev - consume_prev)
        # nächster Verbrauch wächst um Inflation
        consume_prev += inflation*consume_prev
        # Vorbereitung der nächsten Runde
        fortune_2prev = fortune_prev
        fortune_prev = fortune
        year += 1
        # Ausgabe
        yield year, fortune, consume_prev

def main():
    FORTUNE = float(input('Geben Sie das Anfangsvermögen an: '))
    CONSUME = float(input('Wie hoch sind die Ausgaben im ersten Jahr? '))
    INFLATON_PERCENT = float(input('Wie groß ist die Inflation (Prozent)? '))
    INTEREST_PERCENT = float(input('Wie viele Zinsen erhalten Sie jährlich auf das Vermögen (Prozent)? '))
    TAX_PERCENT = float(input('Wie viel Prozent Steuern zahlen Sie jährlich? '))
    # Datei erzeugen
    with open('fortune_tax.txt', 'w', encoding='UTF-8') as outfile:
        outfile.write(f"Jahr {0:>3d}: fortune: {FORTUNE:>10.2f}, consume: {CONSUME:>7.2f}\n")
        for year, fortune, consume in living_from_fortune(FORTUNE, CONSUME, INFLATON_PERCENT, INTEREST_PERCENT, TAX_PERCENT):
            outfile.write(f"Jahr {year:>3d}: fortune: {fortune:>10.2f}, consume: {consume:>7.2f}\n")
            
if __name__ == '__main__':
    main()