import ast
import csv
from datetime import datetime
from pathlib import Path

input_file = Path("data/SerenaWilliamsCareer.js")
output_file = Path("data/serena_matches.csv")

# Read raw JavaScript data
text = input_file.read_text(encoding = "utf-8")
array_text = text.split("=", 1)[1].strip().rstrip(";")
matches = ast.literal_eval(array_text)

# Serena Williams' date of birth
serena_dob = datetime(1981, 9, 26)

cleaned = []

for match in matches:
    match_date = datetime.strptime(match[0], "%Y%m%d")

    # Calculate Serena's age
    serena_age = (match_date - serena_dob).days / 365.2425

    # Calculate opponent's age
    opponent_age = None

    if match[16]:
        opponent_dob = datetime.strptime(match[16], "%Y%m%d")
        opponent_age = (match_date - opponent_dob).days / 365.2425

    # Calculate age difference
    age_difference = None

    if opponent_age is not None:
        age_difference = opponent_age - serena_age

    # Organize cleaned data
    cleaned.append({
        "date": match_date.strftime("%Y-%m-%d"),
        "tournament": match[1],
        "surface": match[2],
        "result": "win" if match[4] == "W" else "loss",
        "opponent": match[11],
        "serena_age": round(serena_age, 2),
        "opponent_age": round(opponent_age, 2) if opponent_age is not None else "",
        "age_difference": round(age_difference, 2) if age_difference is not None else "",
    })

# Save cleaned data as CSV
with output_file.open("w", newline = "", encoding = "utf-8") as file:
    writer = csv.DictWriter(file, fieldnames = cleaned[0].keys())
    writer.writeheader()
    writer.writerows(cleaned)

print(f"Cleaned {len(cleaned)} matches to {output_file}")
print(f"Matches with missing opponent age: {sum(row['opponent_age'] == '' for row in cleaned)}")
