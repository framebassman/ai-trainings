import dspy

class Breakdown(dspy.Signature):
    """
    Given a passage, break down the passage into key ideas.
    Enumerate every key idea in the passage and
    assign it an importance grade
    (High, Medium, or Low).
    """

    passage = dspy.InputField()
    key_ideas: str = dspy.OutputField(
        desc="numbered list of one key idea per line,"
        "followed by its importance grade, "
             "e.g. 1. <Idea here>. High.")
    importance_grades: list[str] = dspy.OutputField(
        desc='list of importance grades, '
             'e.g. ["High", "Medium", "Low"].')
