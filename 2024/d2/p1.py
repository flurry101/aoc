def solve(input):
    c=0
    for line in input.splitlines():
        p=line.split()
        try:
            lvl=[int(x) for x in p]
        except ValueError:
            continue
        inc=all(lvl[i]<lvl[i+1] for i in range(len(lvl)-1))
        dec=all(lvl[i]>lvl[i+1] for i in range(len(lvl)-1))
        q=all(1<=abs(lvl[i]-lvl[i+1]) <= 3 for i in range(len(lvl)-1))
        if (inc or dec) and q:
            c+=1
    print(c)