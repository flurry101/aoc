def ans(l,r):
    ls=sorted(l)
    rs=sorted(r)    
    tot=sum(abs(a-b) for a,b in zip(ls,rs)) 
    return tot

def read(f):
    l=[]
    r=[]
    try:
        with open(f,'r') as file:
            for line in file:
                p=line.strip().split()
                try:
                    if len(p)==2:
                        l.append(int(p[0]))
                        r.append(int(p[1]))
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
    return l,r
l,r = read("file.txt")
print(ans(l,r))