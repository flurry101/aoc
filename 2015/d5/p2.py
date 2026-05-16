def solve(input):
    c=0
    for line in input.splitlines():
        if not any(line[i:i+2] in line[i+2:] for i in range(len(line)-1)):
            continue
        if not any(line[i]==line[i+2] for i in range(len(line)-2)):
            continue
        c+= 1
    print(c)
