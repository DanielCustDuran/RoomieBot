# -*- coding: utf-8 -*-
import mysql.connector


db = mysql.connector.connect(host="localhost",    # tu host
                     user="root",         # tu usuario
                     passwd="1234",  # tu password
                     db="roomie")        # el nombre de la base de datos
cur = db.cursor()
def busqueda(estado,municipio):
	cur.execute("SELECT count(*) as contad,descripcion,precio,numBanos FROM roomie.departamento where estado=%s and municipio=%s group by descripcion,numBanos,precio",(estado,municipio,))
	data = cur.fetchall()
	if len(data) == 0:
		return 0
	else:
		return data[0]

def validar_no_rep(idfa,type_user):
	sql = 'SELECT * from roomie.usuarios where idface=%s and tipo="%s"'%(idfa,type_user)
	cur.execute(sql)
	data = cur.fetchall()
	if len(data) == 0:
		return 0
	else:
		return 1


def insertar(face, tipo, nombre, telefono):
	sql = 'INSERT INTO usuarios (idface, tipo, nombre, telefono) VALUES (%s, "%s", "%s", %s)'%(face, tipo, nombre, telefono)
	val = validar_no_rep(face,tipo)
	if val==0:
		cur.execute(sql)
		db.commit()
		print("se guardo")
	elif val==1:
		print("ya esta en la base de datos, con el tipo de usuario")

def buscar_idAlquiler(id):
    sql = 'SELECT  idusuarios from roomie.usuarios where idface=%s'%(id)
    cur.execute(sql)
    data = cur.fetchone()
    return  data[0]


def insertar_alquiler(idf, calle, cp, col, mun, estado, numint, numext, descrip, numcuart, numban, precio):
	idfb = buscar_idAlquiler(idf)
	sql = 'INSERT INTO usuarios (calle, CP, colonia, municipio, estado, numInterior, numExterior, idusuario, descrip, numCuartos, numBanos, precio) VALUES ("%s", %s, "%s", "%s", "%s", %s, %s, %s, "%s", %s, %s, %s)'%(calle, cp, col, mun, estado, numint, numext, idfb, descrip, numcuart, numban, precio)
	cur.execute(sql)
	db.commit()
	print("se guardo")
# Cerramos cursor
# cur.close()
