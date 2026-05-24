def solve(input):
    for _ in range(50):
        cur,out,c = input[0],[],1
        for dgt in input[1:]:
            if dgt==cur:
                c+=1
            else:
                out.append(str(c)+cur)
                cur=dgt
                c=1
        input="".join(out)+str(c) + cur
    print(len(input))