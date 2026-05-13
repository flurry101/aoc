def solve(input):
    floor =  input.count('(') + input.count(')')*(-1)
    print(floor)