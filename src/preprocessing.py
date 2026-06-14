"""Tokenisation et génération d'embeddings Word2Vec."""

import re
import numpy as np
from gensim.models import Word2Vec


def tokenize(text: str) -> list[str]:
    """Tokenise un message SonarQube en minuscules, sans ponctuation."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s_]", " ", text)
    return text.split()


def get_sentence_embedding(tokens: list[str], model: Word2Vec, size: int) -> np.ndarray:
    """Moyenne des vecteurs Word2Vec pour une liste de tokens."""
    vectors = [model.wv[t] for t in tokens if t in model.wv]
    if not vectors:
        return np.zeros(size)
    return np.mean(vectors, axis=0)


def build_feature_matrix(messages: list[str], model: Word2Vec, size: int) -> np.ndarray:
    """Construit la matrice de features X à partir d'une liste de messages."""
    tokenized = [tokenize(m) for m in messages]
    return np.vstack([get_sentence_embedding(t, model, size) for t in tokenized])
