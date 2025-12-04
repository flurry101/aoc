def read(f):
    l = []
    try:
        with open(f, 'r') as file:
            for line in file:
                p = line.split()
                try:
                    p=[int(x) for x in p] 
                    def is_safe(p):
                        c1=all(p[i]<p[i+1] for i in range(len(p)-1)) or all(p[i]>p[i+1] for i in range(len(p)-1))
                        c2=all(1<=abs(p[i]-p[i+1])<=3  for i in range(len(p)-1))
                        return c1 and c2
                    if is_safe(p):
                        l.append(True)
                    else:
                        for i in range(len(p)):
                            new =p[:i]+p[i+1:]  
                            if is_safe(new):
                                l.append(True)
                                break   
                except ValueError:
                    pass  
    except FileNotFoundError:
        pass  
    return l

r = read("D2\\input.txt")
print(r.count(True))  
