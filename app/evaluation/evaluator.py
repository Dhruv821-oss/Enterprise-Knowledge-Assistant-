import time

from app.rag.assistant import EnterpriseAssistant
from app.evaluation.dataset import TEST_DATA
from app.evaluation.metrics import EvaluationMetrics


class Evaluator:

    def __init__(self):

        self.assistant = EnterpriseAssistant()

    def evaluate(self):

        results=[]

        for sample in TEST_DATA:

            start=time.time()

            prediction=self.assistant.ask(
                sample["question"]
            )

            latency=round(
                time.time()-start,
                2
            )

            similarity=EvaluationMetrics.answer_similarity(

                prediction["answer"],

                sample["expected_answer"]

            )

            precision=EvaluationMetrics.retrieval_precision(

                prediction,

                sample["expected_sources"]

            )

            recall=EvaluationMetrics.source_recall(

                prediction,

                sample["expected_sources"]

            )

            results.append({

                "question":sample["question"],

                "similarity":similarity,

                "precision":precision,

                "recall":recall,

                "confidence":prediction["confidence"],

                "latency":latency

            })

        return results