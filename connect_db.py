import mysql.connector

db = mysql.connector.connect(host="localhost",# tu host
                     user="root",         # tu usuario
                     passwd="1995",  # tu password
                     db="roomie")        # el nombre de la base de datos

cur = db.cursor()

cur.close()

db.close()
