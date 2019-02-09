import datetime
import json
class TelegramContext:
    def __init__(self, config, telegramHelper):
        self.telegramHelper = telegramHelper
        self.botId = config.botId
        self.lastMessageId = None
        self.lastMessageTime = None
        self.lastResponses = None
        self.chatId = config.chatId

    def run(self):
        if self.lastMessageId is None or self.lastMessageIsOld():
            self.postNewMessage()
        responses = self.getReplysForLastSentMessage()
        print(responses)


    def lastMessageIsOld(self):
        today4pm = datetime.datetime.now().replace(hour=16, minute=0, second=0)
        timeDiff = (self.lastMessageTime - today4pm).total_seconds()
        if timeDiff<0:
            return True
        else:
            return False

    def postNewMessage(self):
        data = self.telegramHelper.send_message('sample message', self.chatId);
        data = json.loads(data)
        self.lastMessageId =data.get('result').get('message_id')
        self.lastMessageTime = datetime.datetime.now()
        print(data)

    def getReplysForLastSentMessage(self):
        data = self.telegramHelper.get_updates()
        replys = (list)(filter(lambda result: result.get('message').has_key('reply_to_message'), data.get('result')))
        replysForGivenMessage = (list)(
            filter(lambda response: response.get('message').get('reply_to_message').get('message_id') == self.lastMessageId,
                   replys));
        return replysForGivenMessage;

