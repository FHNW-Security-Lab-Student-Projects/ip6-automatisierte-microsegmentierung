import pandas as pd

from runtime import generate as runtime
from vlans import generate as vlans
from success import generate as success
from constraints import generate as constraints

from pathlib import Path
from pathlib import Path
import shutil


df = pd.read_csv("../experiments/results.csv")

OUTPUT_DIR = Path("plots/output")

def clear_plots():
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

clear_plots()

runtime(df)
vlans(df)
success(df)
constraints(df)

print("All plots generated.")
