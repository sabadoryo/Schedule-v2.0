from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot
from schedule3.models import *

state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.Reset, message_types=[message_types.Text])
def send_group(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = str(update.get_message().get_text())
    subj = Subjects.objects.values_list('title', flat=True)
    all_events = Event.objects.all()
    all_events_stringed = list(map(str, all_events))
    print(bot.getUpdates())
    if text == 'start':
        send_options(bot, chat_id)
    elif text in all_events_stringed:
        state.set_memory({'name': text})
        bot.sendMessage(chat_id,
                        text='Before sending message type first string- `Message`\nExample: Message: Uroka ne budet!\nSend message for a ' + text,
                        parse_mode=bot.PARSE_MODE_MARKDOWN)
    elif text in subj:
        d = Subjects.objects.get(title=text)
        events = Event.objects.filter(subject=d)
        events_buttons = list()
        for i in events:
            events_buttons.append([KeyboardButton.a(str(i))])
        bot.sendMessage(
            chat_id,
            text='Here is a list of events, choose for which one you want to edit a message.',
            reply_markup=ReplyKeyboardMarkup.a(
                one_time_keyboard=True,
                resize_keyboard=True,
                keyboard=events_buttons
            ),
            parse_mode=bot.PARSE_MODE_MARKDOWN
        )
    elif text[:8] == 'Message:':
        kekw = state.get_memory()['name']
        for i in all_events:
            if str(i) == kekw:
                kekw = i
                kekw.message = text[8:]
                kekw.save()
        bot.sendMessage(chat_id,
                        text='All done, checkout the schedule!',
                        parse_mode=bot.PARSE_MODE_MARKDOWN)
    else:
        bot.sendMessage(chat_id,
                        text='Send start to continue',
                        parse_mode=bot.PARSE_MODE_MARKDOWN)
    #
    # d = Subjects.objects.get(title=text)
    # events = Event.objects.filter(subject=d)
    # print(events)
    # bot.sendMessage(
    #     chat_id,
    #     text='Here is list of events choose one',
    #     reply_markup=ReplyKeyboardMarkup.a(
    #         one_time_keyboard=True,
    #         resize_keyboard=True,
    #         keyboard=[[KeyboardButton.a('1')]]
    #     )
    # )


@processor(state_manager, from_states=state_types.All, update_types=[update_types.CallbackQuery])
def handle_callback_query(bot: TelegramBot, update, state):
    callback_data = update.get_callback_query().get_data()
    bot.answerCallbackQuery(update.get_callback_query().get_id(),
                            text='Callback data received: {}'.format(callback_data))


def send_normal_keyboard(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='Here is a keyboard for you!',
        reply_markup=ReplyKeyboardMarkup.a(
            one_time_keyboard=True,
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton.a('Text 1'), KeyboardButton.a('Text 2')],
                [KeyboardButton.a('Text 3'), KeyboardButton.a('Text 4')],
                [KeyboardButton.a('Text 5')]
            ]
        ),
        parse_mode=bot.PARSE_MODE_MARKDOWN
    )


def send_inline_keyboard(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='Here is an inline keyboard for you!',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                [
                    InlineKeyboardButton.a('URL Button', url='https://google.com'),
                    InlineKeyboardButton.a('Callback Button', callback_data='some_callback_data')
                ]
            ]
        )
    )


def send_options(bot, chat_id):
    subj = Subjects.objects.values_list('title', flat=True)
    dfinal = list()
    for i in subj:
        dfinal.append([KeyboardButton.a(i)])
    bot.sendMessage(
        chat_id,
        text='Choose subj: ',
        reply_markup=ReplyKeyboardMarkup.a(
            one_time_keyboard=True,
            resize_keyboard=True,
            keyboard=dfinal
        ),
    )
