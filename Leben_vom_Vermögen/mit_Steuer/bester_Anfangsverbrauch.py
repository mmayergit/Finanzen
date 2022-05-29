'''
Hier wird für verschieden Ausgaben im ersten Jahr ausprobiert, 
wie viele Jahre das Vermögen reicht (muss ja nicht den Erben zufallen...).
'''

from Leben_vom_Vermögen_mit_Steuern import living_from_fortune
import numpy as np
from fortune_plot import read_file
import matplotlib.pyplot as plt

def main():
    FORTUNE = 1e6
    CONSUME = np.linspace(2e4, 1e5, 11)
    INFLATON_PERCENT = 5
    INTEREST_PERCENT = 7
    TAX_PERCENT = 27
    fig, ax = plt.subplots(layout='constrained')
    ax.grid(True)
    counter = 0
    for consume in CONSUME:
        file = f'fortune_tax_{counter:04d}.txt'
        with open(file, 'w', encoding='UTF-8') as outfile:
            outfile.write(f"Jahr {0:>3d}: fortune: {FORTUNE:>10.2f}, consume: {consume:>7.2f}\n")
            for year, fortune, consume_ in living_from_fortune(FORTUNE, consume, INFLATON_PERCENT, INTEREST_PERCENT, TAX_PERCENT):
                outfile.write(f"Jahr {year:>3d}: fortune: {fortune:>10.2f}, consume: {consume_:>7.2f}\n")
        ax.plot(read_file(file), label = '$1^{st}$'+f' cons. = {consume:>7g}')
        counter += 1
    ax.legend()
    ax.set_title('Vergleich verschiedener Ausgaben bei\nSteuer = 27%, Inflation = 5%, Zins = 7%')
    ax.set_ylabel('Vermögen')
    ax.set_xlabel('Jahre')
    plt.savefig('Anfangsverbrauch.png')

if __name__ == '__main__':
    main()