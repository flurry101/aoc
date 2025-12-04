def ans(l,r):
    sim =[]
    for e in l:
        sim.append(e*r.count(e))  
    return sum(sim)
def read(f):
    l = []
    r = []
    try:
        with open(f, 'r') as file:
            for line in file:
                p = line.strip().split()
                try:
                    if len(p) == 2:
                        l.append(int(p[0]))
                        r.append(int(p[1]))
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
    return l, r
l, r = read("file.txt")
print(ans(l, r))