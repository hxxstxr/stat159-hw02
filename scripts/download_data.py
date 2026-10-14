
from pathlib import Path
from urllib.request import Request, urlopen

url = "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js"

data_dir = Path("data")
data_dir.mkdir(parents = True, exist_ok = True)

output_file = data_dir / "SerenaWilliamsCareer.js"

request = Request(
    url,
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.tennisabstract.com/"
    }
)

with urlopen(request) as response:
    output_file.write_bytes(response.read())

print(f"Downloaded successfully: {output_file}")