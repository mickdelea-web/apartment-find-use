import random
import csv

SEED = 4417
rng = random.Random(SEED)

assignments = ["A"] * 60 + ["B"] * 60
rng.shuffle(assignments)

with open("assignments.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["trial", "version"])
    for i, v in enumerate(assignments, start=1):
        w.writerow([i, v])

with open("results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["trial", "version", "date", "answer", "yes_no", "reasoning"])
    for i, v in enumerate(assignments, start=1):
        w.writerow([i, v, "", "", "", ""])

print("Created assignments.csv and results.csv")
print("A:", assignments.count("A"), "B:", assignments.count("B"))
