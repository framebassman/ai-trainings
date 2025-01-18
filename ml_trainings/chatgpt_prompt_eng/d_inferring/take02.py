from ml_trainings.chatgpt_prompt_eng import get_completion
from ml_trainings.d_inferring.take01 import lamp_review

prompt = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
