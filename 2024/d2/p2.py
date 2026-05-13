def is_safe(lvl):
    inc=all(lvl[i]<lvl[i+1] for i in range(len(lvl)-1))
    dec=all(lvl[i]>lvl[i+1] for i in range(len(lvl)-1))
    q=all(1<=abs(lvl[i]-lvl[i+1])<=3 for i in range(len(lvl)-1))
    return (inc or dec) and q

def solve(input):
    c=0
    for line in input.splitlines():
        p=line.split()
        try:
            lvl=[int(x) for x in p]
        except ValueError:
            continue
        if is_safe(lvl):
            c+=1
            continue
        for i in range(len(lvl)):
            new=lvl[:i]+lvl[i+1:]
            if is_safe(new):
                c+=1
                break
    print(c)
