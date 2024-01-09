from chat_gpt_api import get_gpt_answer
from bot_file import BotFile

question = "Хочу бота, который поможет моему инфобизнесу. Я специализурюсь на обучении людей по работе с телеграм каналами."

answer = get_gpt_answer(question)
print(answer)
bot = BotFile(bot_name="info_bot", bot_token="6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM")

for action in answer:
    try:
        command = action['command_action']
    except KeyError:
        command = action.get('button_action', None)

    text = action.get('message_text', '')
    buttons_list = action.get('buttons', [])
    buttons_state = True if buttons_list else False

    handler = bot.add_simple_handler if 'command_action' in action else bot.add_query_handler
    handler(command, text, buttons=buttons_state, buttons_list=buttons_list, ncol=2)
