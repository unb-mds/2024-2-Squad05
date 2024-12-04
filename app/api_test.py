from openai import OpenAI

client = OpenAI(api_key=input("API Key: "))
chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello."}]
)
print(chat_completion)
print()
print(chat_completion.choices[0].message.content)
