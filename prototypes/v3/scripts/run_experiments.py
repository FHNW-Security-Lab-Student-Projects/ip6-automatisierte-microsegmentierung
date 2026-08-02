import subprocess
import csv
from pathlib import Path
import shutil

EXPERIMENTS_DIR = Path("experiments")
LOG_DIR = EXPERIMENTS_DIR / "logs"
CSV_PATH = EXPERIMENTS_DIR / "results.csv"

LOG_DIR.mkdir(parents=True, exist_ok=True)

def clear_logs():
    if LOG_DIR.exists():
        shutil.rmtree(LOG_DIR)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

def extract_metrics(output: str):
    metrics = {}

    for line in output.splitlines():
        if line.startswith("METRIC"):
            try:
                key, value = line.replace("METRIC ", "").split("=")
                metrics[key.strip()] = value.strip()
            except:
                continue

    return metrics


def run_experiment(file: Path):
    print(f"Running: {file}")

    result = subprocess.run(
        # ["python3", "scripts/run_pipeline.py", str(file), "--no-vis"],
        ["python3", "scripts/run_pipeline.py", str(file), ""],
        capture_output=True,
        text=True
    )

    output = result.stdout

    # Save log file
    log_file = LOG_DIR / f"{file.stem}.log"
    with open(log_file, "w") as f:
        f.write(output)

    metrics = extract_metrics(output)

    # Add metadata from path
    metrics["dataset"] = file.name
    metrics["topology"] = file.parent.name

    return metrics


def run_all():
    clear_logs()
    results = []

    for file in EXPERIMENTS_DIR.rglob("*.json"):
        metrics = run_experiment(file)
        results.append(metrics)

    save_csv(results)


def save_csv(results):
    if not results:
        return

    keys = sorted(set().union(*(r.keys() for r in results)))

    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nCSV saved to: {CSV_PATH}")


if __name__ == "__main__":
    run_all()