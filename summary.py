#!/usr/bin/env python3.8

"""
Statistics summary for Pass the Pigs

see pig.txt for the credits for and interepetation of the source data

important finding: ~0.4% of rolls end up with touching pigs
"""

from csv import DictReader
from collections import Counter
from typing import Dict

f = DictReader(open("pig.dat.txt", "r"), delimiter=" ")
black, pink, score = Counter(), Counter(), Counter()
count: int = 0
pos_names: Dict[int, str] = {
    1: "Dot Up",
    2: "Dot Down",
    3: "Trotter",
    4: "Razorback",
    5: "Snouter",
    6: "Leaning Jowler",
    7: "Touching",
}


def add_one(name: str):
    """Assumes that @name@ is consistent between the column header and the Counter name"""
    globals()[name][int(roll[name])] += 1


for roll in f:
    count += 1
    add_one("black")
    add_one("pink")
    add_one("score")

value_table: str = "\t".join(
    ["Result", "Name", "Black", "Black %", "Pink", "Pink %", "Total", "Overall %"]
)
for val in pos_names.keys():
    b: int = black[val]
    p: int = pink[val]
    value_table += "\n" + "\t".join(
        [
            str(x)
            for x in [
                val,
                pos_names[val],
                b,
                round(b / count * 100, 2),
                p,
                round(p / count * 100, 2),
                b + p,
                round((p + b) / (count * 2) * 100, 2),
            ]
        ]
    )

score_table: str = "\n".join(
    ["\t".join(["Score", "Number", "%"])]
    + [
        "\t".join(
            [
                str(x)
                for x in [
                    score_point,
                    score[score_point],
                    round(score[score_point] / count * 100, 2),
                ]
            ]
        )
        for score_point in sorted(score.keys())
    ]
)

print(value_table)
print("\n\n")
print(score_table)
