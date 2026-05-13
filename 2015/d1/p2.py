def solve(input):
    floor=0
    pos=0
    for c in input:
        pos+=1
        if c=='(':
            floor+=1
        else:
            floor-=1
        if floor==-1:
            print(pos)
            return pos
