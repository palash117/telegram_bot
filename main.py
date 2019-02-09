from __future__ import print_function

from TelegramContext import TelegramContext
from configData import ConfigData
from telegram_helper import TelegramHelper
import RepeatedTimer
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

class main:
    def __init__(self):
        self.confiData = ConfigData();
        self.telegramHelper = TelegramHelper(self.confiData.getBotId());
        telegramContext = TelegramContext(self.confiData, self.telegramHelper)
        RepeatedTimer
        # print(confiData.getBotId());
        # # data = telegramHelper.send_message('test2','-316560012')
        # data = telegramHelper.get_updates()
        # responseData = getReplysForMessage(24, data)
        # responseData = (list)(map(lambda  value : [value.get('message').get('text'),value.get('message').get('from').get('first_name')], responseData))
        # print(responseData)
        # print(data)





def getReplysForMessage(messageId, data):
    replys = (list)(filter(lambda result: result.get('message').has_key('reply_to_message'), data.get('result')))
    replysForGivenMessage = (list)(filter(lambda response: response.get('message').get('reply_to_message').get('message_id')== messageId, replys));
    return replysForGivenMessage;
main();

