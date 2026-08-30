"""
Aggregate the ablation results into the tables reported in the thesis.

Reads the per-configuration CSVs written by run_ablation.py and reports
means and standard deviations across the five seeds.
"""

from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent.parent
RUNS = BASE / "output" / "runs"

COLS = ["path_skew", "path_kurt", "pool_skew", "pool_kurt", "sr_w", "sr_w_val"]

df = pd.concat([pd.read_csv(f) for f in sorted(RUNS.glob("results_*.csv"))])

summary = (df.groupby(["config", "loss"])[COLS]
             .agg(["mean", "std"])
             .round(3))

pd.set_option("display.width", 250)
pd.set_option("display.max_rows", 200)
print(summary.to_string())