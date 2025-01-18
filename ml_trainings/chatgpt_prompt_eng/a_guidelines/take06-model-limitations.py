from ml_trainings.chatgpt_prompt_eng import get_completion

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = get_completion(prompt)
print(response)
