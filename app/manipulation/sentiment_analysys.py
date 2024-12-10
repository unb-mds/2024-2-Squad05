from openai import OpenAI
from pydantic import BaseModel


class Sentiment(BaseModel):
    comment: str
    sentiment: str


class Prompts:
    sentiment_analysis_v1 = """Perform sentiment analysis on a given Brazilian Portuguese comment. Determine the sentiment score and output it as a number ranging from 0 to 5, where 0 indicates very negative sentiment and 5 indicates very positive sentiment.

# Steps

1. *Read and Understand the Comment*: Thoroughly read and understand the context and content of the comment.
2. *Identify Sentiment Indicators*: Look for words, phrases, and overall tone that indicate sentiment—positive (e.g., "bom," "excelente"), negative (e.g., "ruim," "horrível"), or neutral (e.g., "ok," "normal").
3. *Assess the Sentiment*: Consider the implications of sentiment indicators and the context provided in the comment to identify the overall sentiment.
4. *Assign a Score*: Based on the analysis, assign a score from 0 (very negative) to 4 (very positive).

# Output Format

The output should be in JSON format specifying the identified sentiment category:
```json
{
  "comment": "[original comment]",
  "sentiment": "[0-4]"
}

# Examples

*Example 1:*

- *Input:* "Que ideia horrível, volte pra escola!"
- *Reasoning:* The words "horrível" (horrible) and "volte pra escola" (go back to school) indicate a strong negative sentiment.
- *Output:*
{
  "comment": "Que ideia horrível, volte pra escola!",
  "sentiment": "0"
}

*Example 2:*

- *Input:* "Adorei a ideia, realmente faz muito sentido esse curso de ação."
- *Reasoning:* The words "adorei" (loved) and "realmente faz sentido" (really makes sense) indicate a strong positive sentiment.
- *Output:*
{
  "comment": "Adorei a ideia, realmente faz muito sentido esse curso de ação.",
  "sentiment": "4"
}

*Example 3:*

- *Input:* "Amei! Só precisar mudar tudo!"
- *Reasoning:* The word "amei" (loved it) could indicate positive sentiment, but the term "só precisa mudar tudo" (you only need to change everything) indicates irony and that the writer had a really negative sentiment.
- *Output:*
{
  "comment": "Amei! Só precisar mudar tudo!",
  "sentiment": "0"
}

*Example 4:*

- *Input:* "Não entendi. O que foi levantado?"
- *Reasoning:* The comment doesn't have any strong wording or context.
- *Output:*
{
  "comment": "Não entendi. O que foi levantado?",
  "sentiment": "2"
}

# Notes

- Neutral comments that neither praise nor criticize explicitly should fall in the 1-3 range.
- Consider linguistic nuances and colloquialisms specific to Brazilian Portuguese.
- Pay attention to context clues that might indicate sarcasm or irony, which can affect the perceived sentiment."""


def get_response(message, sys_prompt):
    client = OpenAI(
        api_key="COLOCAR CHAVE AQUI!!")
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": message},
        ],
        response_format=Sentiment,
    )
    return completion.choices[0].message.parsed


def str_response(sentiment: int):
    data = ["Muito negativo", "Negativo", "Neutro", "Positivo", "Muito positivo"]
    return data[sentiment]


def analyze_sentiment(text: str) -> int:
    result = get_response(text, Prompts.sentiment_analysis_v1)
    try:
        sentiment_value = int(result.sentiment)
        if 0 <= sentiment_value <= 4:
            return sentiment_value
        else:
            raise ValueError
    except ValueError:
        return -1
