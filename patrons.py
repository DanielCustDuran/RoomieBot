# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import app
#import mysql.connector
import conexion

Patrons_dict = {'(hol[aiu]|[Qq]ue|[Oo]p|[kq]\sonda|hola\s[a-z\s]*)': "Hola ;) Bienvenido a RoomieBot ¿que tipo de usuario eres? Inquilino o Alquiler",
				'^[soy\s]*(un\s)*inquilino[.!¡]*$' : "¿Como te llamas?",
				'^([Q|q]uiero\s)*([u|U]n\s)*(([d|D]epartamento)\s|([c|C]uarto)\s)*([e|E]n\s)[a-zA-Z\s,]+([c|C]on\s)*[1-9]+\s([c|C]uartos)$':"Bien",
                '^([mM]i\snombre\ses\s)|([mM]e\sllamo\s)[A-Za-záéíóú.-]+$' : "Cual es numero de telefono especificandolo con guiones ejemplo: 999-999-99-99, si no tienes reponde (no tengo)" ,
                '^[0-9]{3}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}|[nN]o\stengo$' : "Especificame la descripcion de como deseas el departamento, (estado municipio y numero de cuartos que desea).",
                '^[aA]dios|bye|[nN]os\svemos|[hH]asta\sluego|[gG]racias(\spor\stodo)*$' : "Nos vemos, ;) un gusto ayudarte.", 'si' : "Perfecto, contactare al dueño para negociar la renta del departamento :)"
                , '^[¿!¡]*para\sque[!¡¿.,?]*$' : "Son datos necesarios ;)"}

Patrons_Alquiler = {'(hol[aiu]|[Qq]ue|[Oo]p|[kq]\sonda)': "Hola ;) Bienvenido a RoomieBot",
                '^[soy\s]*(un\s)*alquiler[.!¡]*$' : "¿Como te llamas?",
                '^([mM]i\snombre\ses\s)|([mM]e\sllamo\s)[A-Za-záéíóú.-]+$' : "Cual es numero de telefono especificandolo con guiones ejemplo: 999-999-99-99, si no tienes reponde (no tengo)" ,
                '^[0-9]{3}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}|[nN]o\stengo$' : "Ahora deberas ingresar ",
                '^[aA]di[oó]s|bye|[nN]os\svemos|[hH]asta\sluego|[gG]racias(\spor\stodo)*$' : "Nos vemos, ;) un gusto ayudarte.", '^[si\sdeseo\srentar\seste\scuarto]|[si]$' : "Perfecto, contactare al dueño para negociar la renta del departamento :)"
                , '^[¿!¡]*para\sque[!¡¿.,?]*$' : "Son datos necesarios ;)"}


state = ["aguascalientes","baja california","baja california sur","campeche","chiapas","chihuahua","ciudad de mexico","coahuila", "colima","durango",
			"guanaguato","guerrero","hidalgo","jalisco","mexico","michoacan","morelos","nayarit","nuevo leon","oaxaca","puebla","queretaro",
			"quitana roo","san luis potosi","sinaloa","sonora","tabasco","tamaulipas","tlaxcala","veracruz","yucatan","zacatecas"]

type_user = ['inquilino','alquiler']

def buscar(mensaje):
    estado = app.estado(mensaje)
    municipio = app.municipio(mensaje)
    busq = conexion.busqueda(estado,municipio)
    if busq == 0:
        Patrons_dict['^([Q|q]uiero\s)*([u|U]n\s)*(([d|D]epartamento)\s|([c|C]uarto)\s)*([e|E]n\s)[a-zA-Z\s,]+([c|C]on\s)*[1-9]+\s([c|C]uartos)$']= "Lo siento, por el momento no hay disponibles :("
    if busq > 1:
        Patrons_dict['^([Q|q]uiero\s)*([u|U]n\s)*(([d|D]epartamento)\s|([c|C]uarto)\s)*([e|E]n\s)[a-zA-Z\s,]+([c|C]on\s)*[1-9]+\s([c|C]uartos)$']= "Claro si hay :), la descripcion es: "+busq[1]+" y tiene "+str(busq[3])+" baños y el precio por mes es de "+str(busq[2])+" ¿Desea rentar este cuarto?"

    #if busq > 1:lC]uarto)\s)*([e|E]n\s)*[a-zA-Z\s,]+([c|C]on\s)*[1-9]+\s([c|C]uartos)$']= "Hay varias opciones"

