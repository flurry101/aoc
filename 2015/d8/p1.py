def solve(input):
    print(sum(len(line)-len(eval(line)) for line in input.splitlines()))
