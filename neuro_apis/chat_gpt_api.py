import json
from openai import OpenAI

def get_gpt_answer(gpt_request, version="gpt-3.5-turbo"):
    client = OpenAI(
    organization='org-VrtKVSdMrmVo9JJin87Y7Dzi',
    api_key="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"
    )

    completion = client.chat.completions.create(
    model=version,
    messages=[
        {"role": "system", "content": "Я хочу получить четко описанную структуру телеграм бота telebot в json. В названиях кнопок и команд ты должен уложиться в 20 символов. Я буду тебе писать текстовое описание бота, ты должен использовать только такой(не добавляй никаких новых значений и ключей в пример) формат ответа:\n```json\n[{\n\"command_action\": \"Название команды\",\n\"message_text\": \"Текст сообщения на эту команду\",\n\"buttons\":[\"Название кнопки\",\"Название кнопки\"]\n},\n{\n\"button_action\": \"Название кнопки\",\n\"message_text\": \"Пример текста\",\n\"buttons\":[\"Название кнопки\",\"Название кнопки\"]\n}, <описание ВСЕХ остальных элементов, которые есть>]\n```\n  action_command обязательно пишется на английском языке и с маленькой буквы. Если обрабатывается кнопка, то только action_button"},
        {"role": "user", "content": f"{gpt_request}"}
    ]
    )

    return json.loads(completion.choices[0].message.content)
