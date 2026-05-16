def solve(input):
    c=0
    for line in input.splitlines():
        if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
            continue
        if sum(line.count(v) for v in 'aeiou')<3:
            continue
        if not any(line[i]==line[i+1] for i in range(len(line)-1)):
            continue
        c+=1
    print(c)
