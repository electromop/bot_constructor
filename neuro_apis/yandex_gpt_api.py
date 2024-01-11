import requests
import json
import re

def find_json(text):
    index_list = [match.start() for match in re.finditer("```", text)]
    json_text = text[index_list[0]+8:index_list[1]]
    return json.loads(json_text)

def get_gpt_answer(iam_token, gpt_request):
    folder_id = 'b1gjb2nnh6p03cgd1rk6'
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "x-folder-id": folder_id,
        "Content-Type": "application/json"
    }

    data = {
    "modelUri": "gpt://b1gjb2nnh6p03cgd1rk6/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "maxTokens": "2000",
        "temperature": 0.05
    },
    "messages": [
        {
        "text": "Я хочу получить четко описанную структуру бота в json. Я буду тебе писать текстовое описание бота, ты должен использовать только такой(не добавляй никаких новых значений и ключей в пример) формат ответа:\n```json\n[{\n\"command_action\": \"Название команды\",\n\"message_text\": /start\",\n\"buttons\":[\"Название кнопки\",\"Название кнопки\"]\n},\n{\n\"button_action\": \"Название кнопки\",\n\"message_text\": \"Пример текста\",\n\"buttons\":[\"Название кнопки\",\"Название кнопки\"]\n}, <описание ВСЕХ остальных элементов, которые есть>]\n```",
        "role": "system"
        },
        {
        "text": f"{gpt_request}",
        "role": "user"
        }
    ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        text = response.json()["result"]["alternatives"][0]["message"]["text"]
        return(find_json(text))
    else:
        return(f'Произошла ошибка: {response.status_code}')
