import dspy
from hamcrest import assert_that, equal_to

passage = "The global climate crisis continues to escalate, with rising temperatures, melting ice caps, and more frequent natural disasters. Governments and organizations are pushing for renewable energy adoption and stricter environmental regulations to combat these effects. However, the transition is often hindered by economic and political barriers."
summary = "Climate change drives extreme weather, prompting renewable energy adoption despite economic and political hurdles."


class TestMain():
    def test_it_works(self):
        lm = dspy.LM("openai/gpt-4o-mini", max_tokens=250)
        dspy.settings.configure(lm=lm)
        qa = dspy.ChainOfThought("passage: str, summary: str -> sentiment: bool")

        response = qa(question="Does this passage contains summary?")

        assert_that(response.sentiment, equal_to(True))
