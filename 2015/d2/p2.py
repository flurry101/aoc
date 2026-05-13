def solve(input):
    s=0
    for line in input.splitlines():
        l,w,h=[int(i) for i in line.split('x')]
        dims=sorted([l,w,h])
        ribbon=2*(dims[0]+dims[1])+l*w*h
        s+=ribbon
    print(s)
