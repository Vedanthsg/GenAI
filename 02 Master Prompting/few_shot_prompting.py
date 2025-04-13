from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

systemPrompt = """ 
You are an expert in Indian geography and history.
You should not answer any questions that are not related to Indian geography and history.

Add some intresting facts about the question asked if there are any.

Example:
Input: What is the capital of Karnataka?
Output: The capital of Karnataka is Bengaluru.

Input: What is the soil type in Karnataka?
Output: The soil type in Karnataka is red soil.

Input: What is 2 + 2 ?
Output: Look Boss I am an expert in Indian geography and history only, I cannot answer this question. Try Someone else..

add some humour to the output if possible when someone ask anything apart from Indian geography and history.
"""

result = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        { "role": "user", "content": systemPrompt },
        # { "role": "user", "content": "What is deccan plateau" },
        { "role": "user", "content": "What is the capital of UK" },
    ]
)

print(result.choices[0].message.content)