def solve(input):
    vec={'^':1j, 'v':-1j, '>':1, '<':-1}
    pos=[0j,0j]
    vis={0j}
    for i,v in enumerate(input):
        turn=i%2
        pos[turn]+=vec[v]
        vis.add(pos[turn])
    print(len(vis))