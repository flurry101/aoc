import hashlib
def solve(input):
    n=1
    while True:
        s = f"{input}{n}"
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith("00000"):
            print(n)
            break
        n+=1