import sys

def vaksineiballene():
    o = open("input", "r")

    n = int(o.readline().strip())
    doser = int(o.readline().strip())
    vaksinested = {}
    forelder = {}

    # Init
    for _ in range(n):
        i = o.readline()
        navn, sted = i.strip().split()
        vaksinested[navn] = sted
    o.readline()
    for line in o.readlines():
        far, barn = line.strip().split()
        forelder[barn] = far

    antallDoser = doser
    current = forelder.get("Deg", None)

    while current != None:
        if vaksinested[current] == "ballene":
            antallDoser -= 1
        current = forelder.get(current, None)

    return antallDoser

def main():
    print(vaksineiballene())

main()
