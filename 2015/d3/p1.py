def solve(input):
    vec={'^':1j, 'v':-1j, '>':1, '<':-1}
    pos=0j
    vis={pos}
    for v in input:
        pos+=vec[v]
        vis.add(pos)
    print(len(vis))
