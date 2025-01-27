import dspy


class SummaryCorrectness(dspy.Signature):
    """
    Compare a system generated summary to the key ideas in the passage.
    For every key idea supplied,
    assign a binary score based on whether the summary contains it.
    And compute an overall score based on the binary scores.
    """

    key_ideas: str = dspy.InputField(
        desc="key ideas in the passage "
             "for evaluating the summary")
    summary: str = dspy.InputField()
    binary_scores: list[bool] = dspy.OutputField(
        desc="list of binary scores for each key idea, "
             "e.g. [True, False, True]")
    overall_score: float = dspy.OutputField(
        desc="overall score for the summary out of 1.0")

class SummarizeSignature(dspy.Signature):
    """
    Given a passage, generate a summary.
    """

    passage = dspy.InputField(desc="a passage to summarize")
    summary: str = dspy.OutputField(
        desc="a concise summary of the passage")

class Summarize(dspy.Module):
    def __init__(self):
        self.summarize = dspy.ChainOfThought(SummarizeSignature)

    def forward(self, passage: str):
        summary = self.summarize(
            passage=passage
        )
        return summary
