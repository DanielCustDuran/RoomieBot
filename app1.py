# -*- coding: utf-8 -*-
from flask import Flask, request
#import mysql.connector
import json
import requests
import config
import re
#import connect_db
from conexion import insertar
#from patrons import Patrons_dict 
import patrons
#import time
#from threading import Thread

import threading
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



datos=[0,"","",0]
@app.route('/', methods = ['POST'])
def webhook():
    #idface = 0
    #tipe = ""
    #name = ""
    #tel = 0
    var = 0
    cont = 0
    
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    message_text = messaging_event["message"]["text"]
                    long_dict = len(patrons.Patrons_dict)
                    for key in patrons.Patrons_dict.keys() :
                        cont+=1
                        saludo = re.compile(key)
                        #saludo_match = re.match(saludo, message_text)
                        saludo_match = dmatch(saludo,message_text)
                        if saludo_match:
                            var = 1
                            if estado(message_text)!=False:
                                patrons.buscar(message_text)
                            if numero(message_text)!=False:
                                datos[3]=numero(message_text)
                                print datos[3]
                            if tipo(message_text)!=False:
                                datos[1]=tipo(message_text)
                                print datos[1]
                            if nombre(message_text)!=False:
                                datos[2]=nombre(message_text)
                                print datos[2]
                            sender_id = messaging_event["sender"]["id"]
                            #recipient_id = messaging_event["recipient"]["id"]
                            datos[0]=int(sender_id)
                            #send_message(sender_id, patrons.Patrons_dict[key])
                            send_message_thread = threading.Thread(target = send_message(sender_id, patrons.Patrons_dict[key]), )
                            #send_message_thread.start()
                            send_message_thread.start()
                            send_message_thread.join()
                            print "se inicio un nuevo thread " +  str(sender_id)
                            print(datos[0])
                            print(datos[1])
                            print(datos[2])
                            print(datos[3])

                            inser_thread = threading.Thread( target = insertar(datos[0],datos[1],datos[2],datos[3]), )
                            inser_thread.start()
                            if len(str(datos[0]))!=0:
                                if len(datos[1])!=0:
                                    if len(datos[2])!=0:
                                        if len(str(datos[3]))!=0:
                                            print "execute query"
                                            insertar(datos[0],datos[1],datos[2],datos[3])
                                            print "executed query"
                                            datos[0]=0
                                            datos[1]=""
                                            datos[2]=""
                                            datos[3]= 93426032143
                           
                                

                        if var==0 and cont==long_dict:
                            sender_id = messaging_event["sender"]["id"]
                            #recipient_id = messaging_event["recipient"]["id"]
                            send_message(sender_id, "Disculpame :'( no te entiendo")
                            

    return "ok", 200


def estado(cadena):
    i = 0
    sta = ""
    cad = cadena.split()
    for c in patrons.state:
        for ca in cad:
            if c==ca:
                sta = c
                i+=1
    if i>=1:
        return sta
    elif i==0:
        return False

def nombre(mensaje):
    mens = mensaje.split()
    i = 0
    c=0
    name = ""
    for i in mens:
        c+=1
    if c>=2:
        if mens[1]=="nombre" or mens[1]=="Nombre":
            name=mens[3]
            return name
        if mens[1]=="llamo":
            name=mens[2]
            return name
        else:
            return False
    elif c<2:
        return False
def tipo(mensaje):
    mens = mensaje.split()
    i = 0
    tip = ""
    for p in patrons.type_user:
        for ca in mens:
            if p==ca:
                tip = p
                i+=1
    if i>=1:
        return tip
    elif i==0:
        return False
def numero(cad):
    var = 0
    if cad=="no tengo" or cad=="No tengo":
        var=1
    elif cad[0].isdigit():
        cade = cad.replace("-", "")
        for ca in cade:
            if ca.isdigit():
                var=2
    if var==0:
        return False
    elif var==1:
        return 0
    elif var==2:
        return cade

def municipio(cadena):
    i = 0
    cad = cadena.split()
    for c in patrons.state:
        for ca in cad:
            if c==ca:
                i+=1
                pos = cad.index(ca)
    if i>=1:
        return cad[pos-1]
    elif i==0:
        return False

def dmatch(cadena,mensaje):
    mensaje_match = re.match(cadena,mensaje)
    return mensaje_match


if __name__=='__main__':
    app.run(port  = 5000)
