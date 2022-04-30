def main():
    count = 0
    with open("names.txt", "r") as f:
        for k in f.readlines():
            if k.split(" ")[1].strip() == "ballene":
                count += 1
    print(count)

main()