def solve():
    o = open("input", "r")

    _, b = map(int, o.readline().strip().split())
    b += 1
    attempts = 0
    counter = 0

    for i in o:
        curr = i.strip()
        try:
            curr = int(curr)
            if counter + curr <= b:
                counter += curr
            else:
                attempts += 1
        except:
            break

    for i in o:
        attempts += 1

    print(attempts)




solve()