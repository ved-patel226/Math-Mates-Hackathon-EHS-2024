import os

from openai import OpenAI

#This is an app called Math Mate. It helps people solve math problems. The user input '+ user_inp + ' respond with a step by step instruction to solve the math problem. If the subject is not related to a math problem, simply answer with the perspective of Math Mates. Due to app restrictions, please keep your response length to a minimum

class Ask_Ai:

    def __init__():
        pass
    
    def step_by_step(user_i):
        
        client = OpenAI(api_key = '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')

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content':'This is an app called Math Mate. It helps people solve math problems. The user input '+ user_i + ' respond with a step by step instruction to solve the math problem. If the subject is not related to a math problem, simply answer with the perspective of Math Mates. Due to app restrictions, please keep your response length to a minimum'
                }
            ],

            model='gpt-3.5-turbo'
        )

        return chat_completion.choices[0].message.content
    



    def practice_problems(user_inp):
        client = OpenAI(api_key = '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')

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content':'This is an app called Math Mate. It helps people make practice math problems. The user input ' + user_inp + ' respond with 10 practice problems similar to this math problem. If the subject is not related to a math problem, simply answer with the perspective of Math Mates. Due to app restrictions, please keep your response length to a minimum'
                }
            ],

            model='gpt-3.5-turbo'
        )

        return chat_completion.choices[0].message.content


