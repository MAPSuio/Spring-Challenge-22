def main():
    o = open("input", "r")
    tot = 0

    a, b = map(int, o.readline().strip().split())
    while True:
        s1 = set()
        s2 = set()
        for _ in range(a):
            s1.add(int(o.readline().strip()))

        for _ in range(b):
            s2.add(int(o.readline().strip()))

        s3 = s1.intersection(s2)
        tot += sum(s3)

        try:
            a, b = map(int, o.readline().strip().split())
        except:
            break

    print(tot)

if __name__ == "__main__":
    main()