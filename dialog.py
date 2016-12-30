# -*- coding: utf-8 -*-
import json
import logging
import time

# from viberbot import Api
# from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage,
    StickerMessage
)
from message import Message
from viberbot.api.viber_requests import ViberMessageRequest

rev_arr = [u"Отлично!", u"Просто класс", u"Херня какая-то", u"Супер", u"Качество на уровне!", u"Не, ну дичь какая-то...", u"Отлично!", u"Просто класс", u"Херня какая-то", u"Супер", u"Качество на уровне!", u"Не, ну дичь какая-то..."];

def get_response(arg, bot):

  switcher = {
        "Hello": first_menu,
        "categories": categories_sent,
        "about": about,
        "club_carts": club_carts,
        "share": share,
        "contacts": contacts,
        "news": news,
        "reviews": reviews,
        "reviews_display": reviews_display,
    }
  # Get the function from switcher dictionary
  func = switcher.get(arg.message.text, first_menu)
  # Execute the function
  return func(arg, bot)

def first_menu(obj, bot):
  message = TextMessage(text=u"Здравствуйте, " + obj.sender.name)

  picture = PictureMessage(media=obj.sender.avatar, text=u"Отличное фото!)")

  bot.send_messages(obj.sender.id, [message, picture])
  time.sleep(3)
  bot.send_messages(obj.sender.id, categories())

def categories():
  keyboard = Message(keyboard={
    "Type": "keyboard",
    "DefaultHeight": "true",
    "Buttons": [
    {
    "ActionType": "reply",
    "ActionBody": "about",
    "Text": "О нас",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "calendar",
    "Text": "Расписание",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "club_carts",
    "Text": "Клубные карты",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "share",
    "Text": "Акции фитнес-клуба",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "reviews",
    "Text": "Отзывы",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "contacts",
    "Text": "Контакты",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "news",
    "Text": "Новости",
    "TextSize": "regular"
    },
    ]
    }, message_type="text", text=u"Какая категория Вас интересует:")
  return [keyboard]

def categories_sent(obj=None, bot=None):
  bot.send_messages(obj.sender.id, categories())

def about(obj=None, bot=None):
  keyboard = Message(keyboard={
    "Type": "keyboard",
    "DefaultHeight": "true",
    "Buttons": [
    {
    "ActionType": "reply",
    "ActionBody": "about_info",
    "Text": "Информация о клубе",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "about_photo",
    "Text": "Фотогалерея",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "about_coach",
    "Text": "Наши тренеры",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "about_training",
    "Text": "Виды тренировок",
    "TextSize": "regular"
    },
    {
    "ActionType": "reply",
    "ActionBody": "categories",
    "Text": "Возврат в меню",
    "TextSize": "regular"
    },
    ]
    }, message_type="text", text=u"Какая подкатегория Вас интересует:")

  bot.send_messages(obj.sender.id, [keyboard])

def club_carts(obj=None, bot=None):
  message = TextMessage(text=u"***Вывод информации как стать обладателем клубной карты и возможностей клубной карты***")
  bot.send_messages(obj.sender.id, [message])

def share(obj=None, bot=None):
  message = TextMessage(text=u"***Вывод акций***")
  bot.send_messages(obj.sender.id, [message])

def news(obj=None, bot=None):
  message = TextMessage(text=u"***Вывод новостей***")
  bot.send_messages(obj.sender.id, [message])

def contacts(obj=None, bot=None):
  message = TextMessage(text=u"г. Одесса, ул. Комарова, 10, оф.114, тел. 445-089-084,  06784")
  bot.send_messages(obj.sender.id, [message])

def reviews(obj=None, bot=None):
    keyboard = Message(keyboard={
      "Type": "keyboard",
      "DefaultHeight": "true",
      "Buttons": [
      {
      "ActionType": "reply",
      "ActionBody": "reviews_display",
      "Text": "Посмотреть отзывы",
      "TextSize": "regular"
      },
      {
      "ActionType": "reply",
      "ActionBody": "reviews_leave",
      "Text": "Оставить отзыв",
      "TextSize": "regular"
      }
      ]
      }, message_type="text", text=u"Какая подкатегория Вас интересует:")
    bot.send_messages(obj.sender.id, [keyboard])

def reviews_display(obj=None, bot=None):
    message = TextMessage(text='\n'.join(rev_arr))
    keyboard = Message(keyboard={
      "Type": "keyboard",
      "DefaultHeight": "true",
      "Buttons": [
      {
      "ActionType": "reply",
      "ActionBody": "reviews_display_more",
      "Text": "Ещё",
      "TextSize": "regular"
      }
      ]
      }, message_type="text", text=u"Какая подкатегория Вас интересует:")
    bot.send_messages(obj.sender.id, [message, keyboard])

def reviews_leave(obj=None, bot=None):
    message = TextMessage(text="Напишите пожалуйста свой отзыв и отправьте")
    bot.send_messages(obj.sender.id, [message])
