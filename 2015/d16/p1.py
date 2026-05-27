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
        if all(gifts.get(parts[i][:-1]) == int(parts[i + 1])for i in range(2, len(parts), 2)):
            print(int(parts[1][:-1]))
