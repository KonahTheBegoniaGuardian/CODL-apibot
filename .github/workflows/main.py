import requests as requests

url = "https://api.telegram.org/bot906547384:AAE3TYm0Aoxhm1JKqu1vqTk4uwfQgLujCiY/"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), 'Konichiwa! I am CBOT2, hajimemashite! I was made by CODL IND, I am ready for help you!')
            elif get_message_text(update).lower() == "CODL":
                send_message(get_chat_id(update),
                             'CODL is a book wrote by @CODL4A, meaning Chronicles of Dragon Lands')
            else:
                send_message(get_chat_id(update), "I'm sorry, but mine system is being updated by @CODL4A, new commands are missing, please, contact CODL IND for support.")
            update_id += 1


# call the function to make it reply
main()
