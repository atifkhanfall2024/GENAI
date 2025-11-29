from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyDlMThqOFVHZQ5AzuWKOjhoDRwJWFxnnts',
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

response = client.chat.completions.create(
    model='gemini-2.5-pro',
    messages=[
        {"role":"user" , "content":"Hi welcome to me am atif"}
    ]
)


print(response.choices[0].message.content)
