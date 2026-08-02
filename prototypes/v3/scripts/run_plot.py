import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("experiments/results.csv")

df["heuristic_time"] = df["heuristic_time"].astype(float)
df["z3_time"] = df["z3_time"].astype(float)

plt.plot(df["nodes"], df["heuristic_time"], label="Heuristic")
plt.plot(df["nodes"], df["z3_time"], label="Z3")

plt.legend()
plt.xlabel("Nodes")
plt.ylabel("Time (s)")
plt.show()