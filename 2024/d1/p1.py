def solve(input):
    l=[]
    r=[]
    for line in input.splitlines():
        p=line.strip().split()
        if len(p)!=2:
            continue
        try:
            l.append(int(p[0]))
            r.append(int(p[1]))
        except ValueError:
            continue
    tot=sum(abs(ls-rs) for ls,rs in zip(sorted(l),sorted(r)))
    print(tot)
