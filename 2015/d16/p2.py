def solve(input):
    gifts = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for aunt in input.splitlines():
        parts=aunt.replace(",","").split()
        if all(
            (
                int(parts[i+1])>gifts[parts[i][:-1]]
                if parts[i][:-1] in ("cats", "trees")
                else int(parts[i +1])<gifts[parts[i][:-1]]
                if parts[i][:-1] in ("pomeranians","goldfish")
                else int(parts[i + 1])==gifts[parts[i][:-1]]
            ) for i in range(2, len(parts), 2)
        ):
            print(int(parts[1][:-1]))