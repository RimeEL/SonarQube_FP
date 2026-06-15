"""Convert CSV inputs in data/input into processed numpy/joblib files.

Usage: .\venv_sca\Scripts\python.exe scripts\convert_input_to_processed.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import joblib

ROOT = Path('.')
DATA_INPUT = ROOT / 'data' / 'input'
PROCESSED = ROOT / 'data' / 'processed'
PROCESSED.mkdir(parents=True, exist_ok=True)

def load_csv_or_none(p: Path):
    if p is None:
        return None
    if not p.exists():
        return None
    return pd.read_csv(p, header=None).values

def main():
    x_train = load_csv_or_none(DATA_INPUT / 'x_train.csv')
    if x_train is None:
        x_train = load_csv_or_none(DATA_INPUT / 'X_train.csv')

    x_test = load_csv_or_none(DATA_INPUT / 'x_test.csv')
    if x_test is None:
        x_test = load_csv_or_none(DATA_INPUT / 'X_test.csv')

    y_train = load_csv_or_none(DATA_INPUT / 'y_train.csv')
    y_test = load_csv_or_none(DATA_INPUT / 'y_test.csv')

    if x_train is not None:
        np.save(PROCESSED / 'X_train.npy', x_train)
        joblib.dump(x_train, PROCESSED / 'X_train.pkl')
        print('Saved X_train to', PROCESSED / 'X_train.npy')
    if x_test is not None:
        np.save(PROCESSED / 'X_test.npy', x_test)
        joblib.dump(x_test, PROCESSED / 'X_test.pkl')
        print('Saved X_test to', PROCESSED / 'X_test.npy')
    if y_train is not None:
        np.save(PROCESSED / 'y_train.npy', y_train.squeeze())
        joblib.dump(y_train.squeeze(), PROCESSED / 'y_train.pkl')
        print('Saved y_train to', PROCESSED / 'y_train.npy')
    if y_test is not None:
        np.save(PROCESSED / 'y_test.npy', y_test.squeeze())
        joblib.dump(y_test.squeeze(), PROCESSED / 'y_test.pkl')
        print('Saved y_test to', PROCESSED / 'y_test.npy')

    if x_train is None and x_test is None:
        print('No X_train/X_test found in data/input')

if __name__ == '__main__':
    main()
