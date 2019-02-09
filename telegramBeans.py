# coding: utf-8


class Chat:
    def __init__(self, id, first_name, last_name, type, title, all_members_are_administrators):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.title = title
        self.all_members_are_administrators = all_members_are_administrators


class MessageFrom:
    def __init__(self, id, is_bot, first_name, last_name, language_code):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code


class ReplyToMessageFrom:
    def __init__(self, id, is_bot, first_name, username):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username


class ReplyToMessage:
    def __init__(self, message_id, reply_to_message_from, chat, date, text):
        self.message_id = message_id
        self.reply_to_message_from = reply_to_message_from
        self.chat = chat
        self.date = date
        self.text = text


class Message:
    def __init__(self, message_id, message_from, chat, date, text, reply_to_message, group_chat_created):
        self.message_id = message_id
        self.message_from = message_from
        self.chat = chat
        self.date = date
        self.text = text
        self.reply_to_message = reply_to_message
        self.group_chat_created = group_chat_created


class Result:
    def __init__(self, update_id, message):
        self.update_id = update_id
        self.message = message


class Empty:
    def __init__(self, ok, result):
        self.ok = ok
        self.result = result
