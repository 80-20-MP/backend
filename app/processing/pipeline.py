import pickle
import random

import flair
import numpy as np
import pandas as pd
from flair.data import Sentence
from flair.embeddings import TransformerDocumentEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

device = "cpu"
flair.device = device

with open("/server/pickles/popularities.pickle", "rb") as f:
    popularities = pickle.load(f)
with open("/server/pickles/embeddings.pickle", "rb") as f:
    embeddings = pickle.load(f)
with open("/server/pickles/documents.pickle", "rb") as f:
    documents = pickle.load(f)


def get_tags(req: str) -> list[str]:
    max_tags = 10
    count = 10
    similar_count = 0  # must be 0

    querries = get_queries(req, count)
    # can return this if don't have time for history search
    if similar_count == 0:
        return querries

    # THIS PART IS NOT READY

    # simililar_sessions = get_similar_session_best_requests(req, similar_count)
    # recommended_count_each = (max_tags-count)/similar_count
    # for i in range(simililar_sessions):
    #     similar = get_similar_session_best_requests(req, similar_count)
    #     for req in similar:
    #         qq = get_querries(similar, recommended_count_each)
    #         querries.append(qq)

    # return querries


def get_queries(req: str, count: int) -> list[str]:
    # return count querries similar to request
    transformer = TransformerDocumentEmbeddings(
        "sentence-transformers/stsb-xlm-r-multilingual", fine_tune=False
    )

    test_sentences = [Sentence(req)]
    transformer.embed(test_sentences)

    test = random.choice(test_sentences)
    test.to_plain_string()

    distances = cosine_similarity(test.embedding[np.newaxis, :], embeddings)[0]
    distances = distances * popularities

    ratings = np.argsort(-distances).tolist()[:count]

    print(f'Рейтинг подходящих запросов для: "{test.to_plain_string()}"')
    return list(map(documents.__getitem__, ratings))


def get_similar_session_best_requests(req: str, count: int) -> list[str]:
    return [["a", "b"], ["a", "c"], ["a", "d"]]
