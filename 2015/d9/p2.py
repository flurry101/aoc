from itertools import permutations
def solve(input):
    dist={}
    for e in input.splitlines():
        a,_,b,_,d = e.split()
        dist[a,b]=dist[b,a]=int(d)
    print(max(sum(dist[route[i],route[i+1]] for i in range(len(route)-1)) for route in permutations(set(a for a,_ in dist))))