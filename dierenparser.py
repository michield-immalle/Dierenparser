from dataclasses import dataclass


@dataclass
class Dier:
    
    def __init__(self):
        self.naam = ""
        self.soort = ""
        self.aantalPoten = 0
        self.kleur = ""
        self.geluid = ""

def parse_line(line):
    naam, soort, aantalpoten, kleur, geluid = line.split(' - ')
    d = Dier(naam, soort, int(aantalpoten), kleur, geluid)
    return d

def parse_text(str):
    dieren = []
    for line in str.splitlines():
        d = parse_line(line)
        dieren.append(d)
    return dieren


if __name__ == '__main__':
    dieren = []
    with open('dieren.txt', 'r') as f:
        dieren = parse_text(f.read())
    
    for dier in dieren:
        dier.print()
