with open('d1.txt','r') as f:
    dial=50
    c =0
    for l in f.readlines():
        dir = l[0]
        rot = int(l[1:])
        if dir=='R':
            dial=(dial+rot)%100
        elif dir=='L':
            dial=(dial-rot)%100
        if dial==0:
            c+=1
    print(c)