def main():
    o = open("input", "r")
    bord = int(o.readline().strip())
    metern = int(o.readline().strip())

    counter = 0
    peepz = list()
    cap = list()

    for i in o.readlines():
        a, b = map(int, i.strip().split())
        peepz.append(a)
        cap.append(b)

    for i in range(len(peepz)):
        stoy = 0
        if peepz[i] < cap[i]:
            for k in range(i-metern, i+metern+1):
                if (k >= 0) and (k < len(peepz)):
                    stoy += peepz[k]

        counter = max(counter, stoy)

    print(counter)


if __name__ == "__main__":
    main()