import re
def solve(input):
    print(sum(map(int,re.findall(r'-?\d+', input))))