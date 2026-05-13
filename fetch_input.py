import os
import sys
from pathlib import Path
import requests as req
from dotenv import load_dotenv
load_dotenv()

SESSION=os.getenv("AOC_SESSION")
if not SESSION:
    raise Exception("Missing AOC_SESSION")

if len(sys.argv)!=3:
    print("use: python fetch_input.py <year> <day>")
    sys.exit(1)
year = sys.argv[1]
day = sys.argv[2]

folder = Path(f"{year}/d{day}")
folder.mkdir(parents=True, exist_ok=True)

input_file = folder/"input.txt"
if input_file.exists():
    print(f"{input_file} already exists")
    sys.exit(0)

url = f"https://adventofcode.com/{year}/day/{day}/input"
res = req.get(url,headers={
        "Cookie": f"session={SESSION}",
        "User-Agent": "github.com/flurry101/aoc"
    }
)

if res.status_code!=200:
    raise Exception(f"Failed to fetch input ({res.status_code})")
input_file.write_text(res.text.rstrip())

template= """def solve(input):
    pass
"""
(folder/"p1.py").write_text(template)
(folder/"p2.py").write_text(template)
print(f"saved input to {input_file}")