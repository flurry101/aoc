import sys
import importlib
from pathlib import Path

if len(sys.argv)!=4:
    print("use: python run.py <year> <day> <part>")
    sys.exit(1)
year = sys.argv[1]
day = sys.argv[2]
part = sys.argv[3]

input_path = Path(f"{year}/d{day}/input.txt")
data = input_path.read_text().rstrip()
module = importlib.import_module(f"{year}.d{day}.p{part}")
module.solve(data)