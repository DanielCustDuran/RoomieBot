# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import requests
import config
import re
#import connect_db
from patrons import Patrons_dict
app = Flask(__name__)



def send_message(recipient_id, message_text):
    params = {
        "access_token" : config.ACCESS_TOKEN,
    }
    headers = {
            "Content-Type" : "application/json"
    }
    data = json.dumps({
        "recipient" : {
            "id" : recipient_id
        },
        "message" : {
            "text" : message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.10/me/messages", \
				params=params, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)

@app.route('/', methods = ['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == config.VERIFY_TOKEN:
            return "Verication token mismatch",  403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods = ['POST'])
def webhook():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    message_text = messaging_event["message"]["text"]
                    for key in Patrons_dict.keys() :
                        saludo = re.compile(key)
                        saludo_match = re.match(saludo, message_text)
                        if saludo_match:
                            sender_id = messaging_event["sender"]["id"]
                            recipient_id = messaging_event["recipient"]["id"]
                            send_message(sender_id, Patrons_dict[key])
                if messaging_event.get("delivery"):
                    pass
                if messaging_event.get("optin"):
                    pass
                if messaging_event.get("postback"):
                    pass
    return "ok", 200

if __name__=='__main__':
    app.run(port  = 5000)
