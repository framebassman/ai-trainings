import dspy

from ai_trainings.dspy_experiments.summarization.program import start

# start()

lm = dspy.LM("openai/gpt-4o-mini", max_tokens=250)
dspy.settings.configure(lm=lm)

# Define a module (ChainOfThought) and assign it a signature (return an answer, given a question).
qa = dspy.ChainOfThought('question -> answer')

# Run with the default LM configured with `dspy.configure` above.
response = qa(question="How many floors are in the castle David Gregory inherited?")
print(response.answer)
