def main():
    o = open("input", "r")
    a, b = map(int, o.readline().strip().split())
    tot = 0

    for i in o.readlines():
        tot += min(b + 1, int(i.strip()))

    print(tot)



if __name__ == "__main__":
    main()