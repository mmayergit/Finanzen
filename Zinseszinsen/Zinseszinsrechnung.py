'''
Die Implementierung entspricht der Bearbeitung einer Aufgabe aus:
Langtangen, Hans Petter(2016): A Primer on Scientific Programming with Python,
(= Texts in Computational Science and Engineering, Bd. 6),
Springer: Berlin / Heidelberg, 5. Auflage.

Es wird die Zinseszinsrechnung simuliert, die man vermutlich auch schon aus der Schule kennt:
x_n = x_n-1 + p/100*x_n-1
Hierbei ist x_n das angelegte Kapital im n-ten Jahr, x_n-1 das Kapital aus dem Jahr davor und p die jährliche Zinsrate.

Es können X0 (Anfangskapital), P (jährlicher Zinssatz) und N (Dauer der Anlage) angegeben werden.
Es wird ein Textdokument erzeugt, das die Entwicklung der Anlage zeigt.
'''
def sequence(x0, p, N):
    n = 0
    x_nm1 = x0
    while n < N:
        x_n = x_nm1 + p/100*x_nm1
        x_nm1 = x_n
        n += 1
        yield n, x_n

def main():
    X0 = 100
    P = 5
    N = 20
    with open('growth.txt', 'w') as outfile:
        outfile.write(f"Jahr {0:>3d}: {X0:>8.2f}\n")
        for year, amount in sequence(X0, P, N):
            outfile.write(f"Jahr {year:>3d}: {amount:>8.2f}\n")

if __name__ == '__main__':
    main()