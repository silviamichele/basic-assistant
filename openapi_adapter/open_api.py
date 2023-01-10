import openai

from settings.settings import settings

openai.api_key = settings.OPEN_API_KEY


def open_api_search(prompt: str) -> str:
    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7
    )

    open_ai_answer = response.choices[0].text

    return open_ai_answer
    
    
