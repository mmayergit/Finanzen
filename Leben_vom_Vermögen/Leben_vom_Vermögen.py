'''
Simuliert wird die Entwicklung eines Vermögens x im Verlauf von n Jahren.

Vom Vermögen geht jedes Jahr ein Betrag zur Lebenshaltung ab, andererseits kommen Zinsen dazu:
x_n = x_n-1 - c_n-1
x_n = x_n + x_n*p/100
Dabei ist x_n das Vermögen nach n Jahren, x_n-1 das Vermögen im Jahr davor, c_n-1 der Verbrauch im Jahr davor und p der Jahreszinssatz in Prozent.

Der Verbrauch steigt jedes Jahr durch die Inflation:
c_n = c_n-1 + I/100*c_n-1
I ist die Inflationsrate in Prozent, die den Verbrauch steigen lässt.

Der Startwert für das Vermögen ist FORTUNE, der Startwert für den Verbrauch ist CONSUME.

Es wird eine Text-Datei erzeugt, die für jedes Jahr den berechneten Vermögenswert und die berechneten Ausgaben auflistet.
'''

def living_from_fortune(initial_fortune, consume_initial, inflation_loss, interest_gain):
    # Umrechnung von Prozent auf Dezimal
    interest = interest_gain/100
    inflation = inflation_loss/100
    # Anfangsverbrauch
    consume_prev = consume_initial
    # Anfangsvermögen
    fortune_prev = initial_fortune
    # Anfangsjahr
    year = 0
    # Simulation
    while fortune_prev >= 0 and year <= 50:
        # Vermögen plus Zinsen minus Verbrauch
        fortune = fortune_prev - consume_prev
        fortune += interest*fortune
        # nächster Verbrauch wächst um Inflation
        consume_prev += inflation*consume_prev
        # Vorbereitung der nächsten Runde
        fortune_prev = fortune
        year += 1
        # Ausgabe
        yield year, fortune, consume_prev

def main():
    # Anfangsvermögen
    FORTUNE = float(input('Geben Sie das Anfangsvermögen an: '))
    # Prozent der Zinsen vom ersten Jahr, die man verbraucht
    CONSUME = float(input('Wie hoch sind die Ausgaben im ersten Jahr? '))
    # jährliche Inflation
    INFLATON_PERCENT = float(input('Wie groß ist die Inflation (Prozent)? '))
    # jährliche Zinsen aufs Vermögen
    INTEREST_PERCENT = float(input('Wie viele Zinsen erhalten Sie jährlich auf das Vermögen (Prozent)? '))
    # Datei erzeugen
    with open('fortune.txt', 'w', encoding='UTF-8') as outfile:
        outfile.write(f"Jahr {0:>3d}: fortune: {FORTUNE:>10.2f}, consume: {CONSUME:>7.2f}\n")
        for year, fortune, consume in living_from_fortune(FORTUNE, CONSUME, INFLATON_PERCENT, INTEREST_PERCENT):
            outfile.write(f"Jahr {year:>3d}: fortune: {fortune:>10.2f}, consume: {consume:>7.2f}\n")
            
if __name__ == '__main__':
    main()