def solve(input):
    s=0
    for line in input.splitlines():
        s+=len(line)+2+line.count('"')+line.count('\\')-len(line.strip())
    print(s)