from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=input("API Key: "))


class Sentiment(BaseModel):
    comment: str
    sentiment: str


class Prompts:
    system = """Perform sentiment analysis on comments written in Brazilian Portuguese, determining whether the sentiment expressed is positive, negative, or neutral.

# Steps

1. **Read and Understand the Comment**: Thoroughly read and understand the context and content of the comment.
2. **Identify Sentiment Indicators**: Look for words, phrases, and overall tone that indicate sentiment—positive (e.g., "bom," "excelente"), negative (e.g., "ruim," "horrível"), or neutral (e.g., "ok," "normal").
3. **Assess the Sentiment**: Consider the implications of sentiment indicators and the context provided in the comment to identify the overall sentiment.
4. **Determine Sentiment Category**: Based on the assessment, categorize the sentiment as positive, negative, or neutral.

# Output Format

The output should be in JSON format specifying the identified sentiment category:
```json
{
  "comment": "[original comment]",
  "sentiment": "[positive/negative/neutral]"
}
```

# Examples

**Example 1:**

- **Input:** "Adorei o filme, foi muito bom!"
- **Reasoning:** The word "adorei" (loved) indicates a strong positive sentiment. "Foi muito bom" (it was very good) further supports this positive sentiment.
- **Output:** 
  ```json
  {
    "comment": "Adorei o filme, foi muito bom!",
    "sentiment": "positive"
  }
  ```

**Example 2:**

- **Input:** "O serviço foi péssimo e demorou demais."
- **Reasoning:** The word "péssimo" (awful) indicates a strong negative sentiment, and "demorou demais" (took too long) supports this negative view.
- **Output:** 
  ```json
  {
    "comment": "O serviço foi péssimo e demorou demais.",
    "sentiment": "negative"
  }
  ```

**Example 3:**

- **Input:** "O evento foi normal, nada de especial."
- **Reasoning:** The word "normal" (normal) and "nada de especial" (nothing special) indicate a neutral sentiment as the commenter shows no strong feelings.
- **Output:** 
  ```json
  {
    "comment": "O evento foi normal, nada de especial.",
    "sentiment": "neutral"
  }
  ```

# Notes

- Consider linguistic nuances and colloquialisms specific to Brazilian Portuguese.
- Pay attention to context clues that might indicate sarcasm or irony, which can affect the perceived sentiment."""


def get_response(message, sys_prompt, example=None):
    if example is None:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": message},
            ],
            response_format=Sentiment,
        )
        return completion.choices[0].message.parsed
    else:
        ...


def sentiment_analysis(message):
    return get_response(message, Prompts.system)


while True:
    user_input = input("User: ")
    response = sentiment_analysis(user_input)
    print(f"Bot: {response.sentiment}")
