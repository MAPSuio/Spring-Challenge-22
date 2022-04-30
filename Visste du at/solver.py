def main():
    cntr = 0
    bingo = ["Ole-Johan Dahl", "Kristen Nygaard", "Simula", "OOP"]

    with open("ord.txt", "r") as f:
        for i in f:
            g = i.strip()
            for t in bingo:
                cntr += g.count(t)

    print(cntr)

main()