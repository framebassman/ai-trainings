import json
import sys

import dspy

from ml_trainings.dspy_experiments.summarization.metric import Metric
from ml_trainings.dspy_experiments.summarization.summary_correctness import Summarize

def start():
    lm = dspy.LM("openai/gpt-4o-mini", max_tokens=250)
    dspy.settings.configure(lm=lm)

    dataset = []

    with open('ml_trainings/dspy_experiments/summarization/dataset.json', 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
        for object in data:
            passage = object.get("passage", "")
            summary = object.get("summary", "")
            score = object.get("score", 0)

            example = dspy.Example(passage=passage, summary=summary, score=score)
            dataset.append(example)

    trainset = [x.with_inputs("passage") for x in dataset]

    def metric(gold, pred, trace=None):
        metric_program = Metric()
        examp = dspy.Example(passage=gold.passage)
        predicted = dspy.Example(summary=pred)
        pred_score = metric_program(example=examp, pred=predicted)
        gold_score = gold.score
        # check if they are almost equal
        return abs(float(gold_score) - float(pred_score)) < 0.2

    program = Summarize()

    evaluate = dspy.Evaluate(devset=trainset, metric=metric,
                             display_progress=True,
                             display_table=True, provide_traceback=True)

    res = evaluate(program, devset=trainset)
    print(res)
