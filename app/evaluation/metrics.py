import time
from difflib import SequenceMatcher


class EvaluationMetrics:

    @staticmethod
    def answer_similarity(predicted, expected):
        return round(
            SequenceMatcher(
                None,
                predicted.lower(),
                expected.lower()
            ).ratio(),
            3
        )

    @staticmethod
    def retrieval_precision(result, expected_sources):

        retrieved = {
            s["document"]
            for s in result["sources"]
        }

        expected = set(expected_sources)

        if len(retrieved) == 0:
            return 0

        return round(
            len(retrieved & expected) /
            len(retrieved),
            3
        )

    @staticmethod
    def source_recall(result, expected_sources):

        retrieved = {
            s["document"]
            for s in result["sources"]
        }

        expected = set(expected_sources)

        return round(
            len(retrieved & expected) /
            len(expected),
            3
        )

    @staticmethod
    def confidence(result):

        return result["confidence"]