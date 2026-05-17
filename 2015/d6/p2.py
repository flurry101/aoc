def solve(input):
    grid = [[0]*1000 for _ in range(1000)]
    for i in input.splitlines():
        if i.startswith('turn on'):
            _,_,c1,_,c2 = i.split()
            op='on'
        elif i.startswith('turn off'):
            _,_,c1,_,c2 = i.split()
            op='off'
        else:
            _,c1,_,c2 = i.split()
            op='toggle'
        x1,y1 = map(int,c1.split(','))
        x2,y2 = map(int,c2.split(','))
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                if op=='on':
                    grid[x][y] +=1
                elif op=='off':
                    grid[x][y] = max(0,grid[x][y]-1)
                else:
                    grid[x][y]+=2
    print(sum(sum(r) for r in grid))
