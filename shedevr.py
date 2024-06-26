import requests
import base64
import time
from random import randint

def generate_image(prompt_text):
    promt = {
          "modelUri": "art://b1g3f13cj7d6d3ss2md9/yandex-art/latest",
          "generationOptions": {
            "seed": randint(1, 20000000),
          },
          "messages": [
            {
              "weight": 1,
              "text": prompt_text
            }
          ]
      }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"

    headers = {
          "Content-Type": "application/json",
          "Authorization": "Api-Key AQVNy07LcVvM2d6W_-sH-4jfymTfPqrkNUfEEw1R"
      }

    response = requests.post(url= url, headers=headers, json=promt)
    result = response.json()
    print(result)

    operation_id = result['id']

    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

    while True:
        operation_response = requests. get(operation_url, headers=headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            time.sleep(5)