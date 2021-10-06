import requests
from config import load_config


def get_update(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    return requests.get(url)


def send_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    return requests.get(url)


def test_bot():
    config = load_config("config.yaml")

    bot_token = config["telegram"]["token"]
    chat_id = config["telegram"]["chat_id"]

    if not bot_token or not chat_id:
        print("no token or no chat_id")
        return

    text = "Hello!\ntest from python"
    r = send_message(text, bot_token, chat_id)
    print(r.status_code)


def get_chat_id():
    config = load_config("config.yaml")
    bot_token = config["telegram"]["token"]

    if not bot_token:
        print("no token")
        return

    r = get_update(bot_token)
    print(r.json())


if __name__ == "__main__":
    get_chat_id()
    test_bot()
