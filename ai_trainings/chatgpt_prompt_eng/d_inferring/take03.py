from ai_trainings.chatgpt_prompt_eng import get_completion
from ai_trainings.d_inferring.take01 import lamp_review

prompt = f"""
Is the writer of the following review expressing anger?\
The review is delimited with triple backticks. \
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
