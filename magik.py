import requests

async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://b1g3f13cj7d6d3ss2md9/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.3,
            "maxTokens": "1000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - нейронная сеть, которая помогает улучшать промт"
                        "Ты получаешь сообщение для пользователя и создаешь один единственный вариант переписанного этого сообщения"
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type: application/json"
        "Authorization": "Api-Key Api-Key AQVNy07LcVvM2d6W_-sH-4jfymTfPqrkNUfEEw1R"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    magik_prompt = result['result']['alternatives'][0]['message']['text']
    return magik_prompt
