from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        { "role": "user", "content": "What is the capital of karnataka" } # Zero Shot Prompting
    ]
)

print(result.choices[0].message.content)