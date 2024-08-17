import os
from mistralai import Mistral


os.environ["MISTRAL_API_KEY"] = "saeskAjvft3QWypk0AOc3xPD6wJHNj9m"

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def get_response(input):

    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": input,
            },
        ]
    )
    print(chat_response.choices[0].message.content)