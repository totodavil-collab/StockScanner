import os
import csv

folder = "history"

stats = {}

for filename in os.listdir(folder):

    if filename.endswith(".csv"):

        filepath = os.path.join(folder, filename)

        with open(filepath, encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                symbol = row["Symbol"]

                if symbol not in stats:
                    stats[symbol] = 0

                stats[symbol] += 1

print("\n🔥 หุ้นที่ติดอันดับบ่อยที่สุด\n")

sorted_stats = sorted(
    stats.items(),
    key=lambda x: x[1],
    reverse=True
)

for symbol, count in sorted_stats:

    print(
        f"{symbol:6} ติดอันดับ {count} วัน"
    )

import os
import csv

folder = "history"

stats = {}

for filename in os.listdir(folder):

    if filename.endswith(".csv"):

        filepath = os.path.join(folder, filename)

        with open(filepath, encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                symbol = row["Symbol"]

                if symbol not in stats:
                    stats[symbol] = 0

                stats[symbol] += 1

