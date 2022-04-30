def main():
    count = 0
    with open("input", "r") as f:
        cntr = 0
        for k in f:
            cntr += 1
            if k.strip() == "crush":
                break
            elif k.strip() == "venn":
                count = cntr

    print(count-1)

main()