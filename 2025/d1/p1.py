def solve(input):
    dial=50
    c =0
    for l in input.splitlines():
        if not l:
            continue
        dirn=l[0]
        rot=int(l[1:])
        if dirn=="R":
            dial=(dial+rot)%100
        elif dirn=="L":
            dial=(dial-rot)%100
        if dial==0:
            c+=1
    print(c)
