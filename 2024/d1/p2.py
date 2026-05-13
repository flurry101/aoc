def solve(input):
    l=[]
    r=[]
    for line in input.splitlines():
        p=line.split()
        if len(p)!=2:
            continue
        try:
            l.append(int(p[0]))
            r.append(int(p[1]))
        except ValueError:
            continue
    score=0
    for e in l:
        score+=e*r.count(e)
    print(score)