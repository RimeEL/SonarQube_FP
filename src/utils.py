"""Métriques et helpers communs."""

import json
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


def evaluate(y_true, y_pred, y_prob=None) -> dict:
    """Retourne un dictionnaire de métriques de classification."""
    report = classification_report(y_true, y_pred, output_dict=True)
    result = {
        "classification_report": report,
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }
    if y_prob is not None:
        result["roc_auc"] = roc_auc_score(y_true, y_prob)
    return result


def save_results(results: dict, path: str) -> None:
    """Sauvegarde les résultats dans un fichier JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Résultats sauvegardés : {path}")


def load_results(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
