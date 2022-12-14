import sys
import subprocess
import pandas as pd

T = [0, 1, 2, 4, 8, 12, 16]
N = [5000000, 1000000]
data = dict()
index = []

print("\nRun bigN exper\n")
for n in N:
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{n}", "-t", f"{t}"], capture_output=True)
        cur_array.append(cur.stdout.decode('utf-8'))
        print(f"node: {n}, t: {t}, time: {cur.stdout.decode('utf-8')}\n")
    data[n] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv("experiment_bigN.csv")