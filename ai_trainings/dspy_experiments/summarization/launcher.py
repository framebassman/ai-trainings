import dspy

from ai_trainings.dspy_experiments.summarization.program import start

# start()

lm = dspy.LM("openai/gpt-4o-mini", max_tokens=250)
dspy.settings.configure(lm=lm)

# # Define a module (ChainOfThought) and assign it a signature (return an answer, given a question).
# qa = dspy.ChainOfThought('question -> answer')
#
# # Run with the default LM configured with `dspy.configure` above.
# response = qa(question="How many floors are in the castle David Gregory inherited?")
# print(response.answer)


passage = "The global climate crisis continues to escalate, with rising temperatures, melting ice caps, and more frequent natural disasters. Governments and organizations are pushing for renewable energy adoption and stricter environmental regulations to combat these effects. However, the transition is often hindered by economic and political barriers."
summary = "Climate change drives extreme weather, prompting renewable energy adoption despite economic and political hurdles."

qa = dspy.ChainOfThought("passage: str, summary: str -> sentiment: bool")

response = qa(question="Does this passage contains summary?")

print(response.sentiment)
