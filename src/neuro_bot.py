from neuro_apis.chat_gpt_api import get_gpt_answer
from bot_file import BotFile

# question = "Хочу бота, который поможет моему инфобизнесу. Я специализурюсь на обучении людей по работе с телеграм каналами."

bot = BotFile(bot_name="hui_bot", bot_token="6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM")

def gen_bot_from_request(question:str, bot:BotFile):
    print("отправил запрос к гпт")
    print(question)
    answer = get_gpt_answer(question)
    print("ответ сформирован")
    print(answer)
    for action in answer:
        try:
            command = action['command_action']
        except KeyError:
            command = action.get('button_action', None)

        text = action.get('message_text', '')
        buttons_list = action.get('buttons', [])
        buttons_state = True if buttons_list else False

        handler_type = "simple" if 'command_action' in action else "callback"
        bot.add_handler(handler_type, command, text, buttons=buttons_state, buttons_list=buttons_list, ncol=2)
    return False

# gen_bot_from_request("Хочу бота для инфобизнеса", bot)
    
