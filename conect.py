# -*- coding: utf-8 -*-
#!/usr/bin/env python
import mysql.connector

db = mysql.connector.connect(host="localhost",    # tu host
                     user="root",         # tu usuario
                     passwd="1234",  # tu password
                     db="roomie")        # el nombre de la base de datos
cur = db.cursor()
a=0



#print(cadena.split())
#cad = cadena.replace("-", "")
#cade = int(cad)
#print(cade)

#sql = 'SELECT count(*), descripcion,numBanos FROM roomie.departamento where estado=%s and municipio=%s group by descripcion',(estado,municipio,numBanos,)

#cur.execute(sql)
#data = cur.fetchall()
#if len(data) != 0:
#	print(data)
#def validar_no_rep(idfa,type_user):
#	sql = 'SELECT * from roomie.usuarios where idface=%s and tipo="%s"'%(idfa,type_user)
#	cur.execute(sql)
#	data = cur.fetchall()
#	if len(data) == 0:
#		return 0
#	else:
#		return 1
idface = 1241243
tipe = "inquilino"
name = "fran"
tel = 124214124

def insertar(face, tipo, nombre, telefono):
	sql = 'INSERT INTO usuarios (idface, tipo, nombre, telefono) VALUES (%s, "%s", "%s", %s)'%(face, tipo, nombre, telefono)
	cur.execute(sql)
	db.commit()
	print("se guardo")
	db.close()
	#cur.close()
insertar(idface,tipe,name,tel)





