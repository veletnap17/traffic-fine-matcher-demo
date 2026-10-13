"""Run the public demo without credentials, a database, or API calls."""
from pathlib import Path
import pandas as pd
from src.matcher import match_fines_to_orders

BASE = Path(__file__).resolve().parents[1]

def run():
    fines = pd.read_csv(BASE / 'demo' / 'fines.csv', parse_dates=['offense_datetime'])
    rentals = pd.read_csv(BASE / 'demo' / 'rentals.csv', parse_dates=['rentstartdatetime', 'enddatetime'])
    matched, unmatched = match_fines_to_orders(fines, rentals)
    dest = BASE / 'output'
    dest.mkdir(exist_ok=True)
    matched.to_csv(dest / 'matched.csv', index=False)
    unmatched.to_csv(dest / 'unmatched.csv', index=False)
    print(f'Matched: {len(matched)}; unmatched: {len(unmatched)}')

if __name__ == '__main__':
    run()
