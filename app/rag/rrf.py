from collections import defaultdict


def reciprocal_rank_fusion(rank_lists, k=60):

    scores = defaultdict(float)

    docs = {}

    for ranking in rank_lists:

        for rank, doc in enumerate(ranking):

            key = (
                doc.metadata["source"],
                doc.metadata["page"],
                hash(doc.page_content)
            )

            docs[key] = doc

            scores[key] += 1 / (k + rank + 1)

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        docs[key]
        for key, _ in ranked
    ]