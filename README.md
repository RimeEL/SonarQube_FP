# SonarQube False Positive Detection

Classification automatique des faux positifs SonarQube par Machine Learning (Random Forest & LightGBM), basée sur le dataset public **"Static Code Analysis Alarms Filtering Reloaded"** (Hegedűs & Ferenc, 2022, IEEE Access).

## Structure du projet

```
SonarQube_FP/
├── data/
│   ├── raw/          # main_dataset.csv + systems.txt (à télécharger — voir ci-dessous)
│   └── input/        # features pré-calculées x_train/x_test (à télécharger — voir ci-dessous)
├── models/
│   └── gensim/       # modèle Word2Vec pré-entraîné (inclus)
├── results/
│   ├── best_10fold_metrics.pkl   # métriques de référence de l'article
│   ├── results_by_types.csv      # performances par règle squid
│   └── dump_metrics.py           # script pour lire le pkl
├── notebooks/
│   ├── 01_exploration.ipynb      # exploration du dataset
│   ├── 02_features.ipynb         # validation du split de features
│   ├── 03_random_forest.ipynb    # entraînement Random Forest
│   └── 04_lightgbm.ipynb         # entraînement LightGBM
├── src/
│   ├── preprocessing.py          # tokenisation et embeddings Word2Vec
│   └── utils.py                  # métriques et helpers
└── requirements.txt
```

## Dataset

Les fichiers de données ne sont pas inclus dans ce dépôt en raison de leur taille. Télécharge le package complet depuis Zenodo :

**Lien** : https://doi.org/10.5281/zenodo.6385770

Après extraction, place les fichiers comme suit :

| Fichier du package | Destination dans le projet |
|---|---|
| `main_dataset.csv` | `data/raw/main_dataset.csv` |
| `systems.txt` | `data/raw/systems.txt` |
| `input/x_train.csv` | `data/input/x_train.csv` |
| `input/x_test.csv` | `data/input/x_test.csv` |
| `input/y_train.csv` | `data/input/y_train.csv` |
| `input/y_test.csv` | `data/input/y_test.csv` |
| `gensim/*.model` | `models/gensim/` |
| `results/best_10fold_metrics.pkl` | `results/best_10fold_metrics.pkl` |
| `results/results_by_types.csv` | `results/results_by_types.csv` |
| `results/dump_metrics.py` | `results/dump_metrics.py` |

## Installation

```bash
python -m venv venv_sca
# Windows
venv_sca\Scripts\activate
# Linux/Mac
source venv_sca/bin/activate

pip install -r requirements.txt
```

## Résultats de référence (article)

| Modèle | Accuracy | Precision | Recall | F1 | AUC |
|---|---|---|---|---|---|
| Decision Tree | — | — | — | — | — |
| **Random Forest** | **0.910** | **0.874** | **0.760** | **0.813** | **0.955** |
| Naive Bayes | — | — | — | — | — |
| Neural Net | — | — | — | — | — |

## Structure des features (480 colonnes)

- **160 colonnes** : one-hot encoding de la règle SonarQube (`squid`)
- **320 colonnes** : embeddings Word2Vec (5 lignes de contexte × 64 dimensions)

## Référence

> Hegedűs, P., & Ferenc, R. (2022). *Static Code Analysis Alarms Filtering Reloaded: A New Real-World Dataset and Its ML-Based Utilization*. IEEE Access, 10, 55090–55101. https://doi.org/10.1109/ACCESS.2022.3176930