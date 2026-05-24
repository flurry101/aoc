import json, re
def solve(input):
    obj = json.loads(input, object_hook=lambda d:{} if "red" in d.values() else d)
    print(sum(map(int,re.findall(r'-?\d+', str(obj)))))

