'''
Liest aus den Dateien fortune_tax.txt und fortune.txt jeweils den Wert von fortune aus
und plottet ihn gegen die Jahre.

Es zeigt sich dann der Einfluss der Steuer auf das Vermögen.
'''

import matplotlib.pyplot as plt

def read_file(filename):
    fortune_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            fortune = float(line.split(',')[0][-10:])
            fortune_list.append(fortune)
    return fortune_list

def main():
    fortune_without_tax = read_file('fortune.txt')
    fortune_with_tax = read_file('fortune_tax.txt')
    fig, ax = plt.subplots(layout='constrained')
    ax.plot(fortune_without_tax, 'r-', label='without tax')
    ax.plot(fortune_with_tax, 'k-', label='with tax = 27%')
    ax.legend()
    ax.set_title('Vergleich: Vermögensentwicklung mit und ohne Steuer')
    ax.set_ylabel('Vermögen')
    ax.set_xlabel('Jahre')
    plt.savefig('Vergleich.png')

if __name__ == '__main__':
    main()