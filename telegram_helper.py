import json
import requests

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace
class TelegramHelper:
    def __init__(self,token):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot{}/".format(self.TOKEN)


    def get_url(self,url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content


    def get_json_from_url(self,url):
        content = self.get_url(url)
        js = json.loads(content)
        return js


    def get_updates(self):
        url = self.URL + "getUpdates"
        js = self.get_json_from_url(url)
        return js


    def get_last_chat_id_and_text(self,updates):
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        return (text, chat_id)


    def send_message(self,text, chat_id):
        url = self.URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        return self.get_url(url)


    # text, chat = get_last_chat_id_and_text(get_updates())
    # send_message(text, chat)