def solve(input):
    s=0
    for line in input.splitlines():
        l,w,h=[int(i) for i in line.split('x')]
        sa=2*(l*w+w*h+h*l)+ min(l*w,w*h,l*h)
        s+=sa
    print(s)