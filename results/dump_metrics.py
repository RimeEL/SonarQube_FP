import os
import pickle
import numpy as np


def load(name):
    with open(name, 'rb') as f:
        return pickle.load(f)
        
print(load('best_10fold_metrics.pkl'))