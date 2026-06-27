from app.evaluation.evaluator import Evaluator
from app.evaluation.report import ReportGenerator


evaluator=Evaluator()

results=evaluator.evaluate()

ReportGenerator.generate(results)