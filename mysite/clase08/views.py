from django.shortcuts import render
from django.http import HttpResponse
import pymysql

db = pymysql.connect('localhost', 'root', '', 'django')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

sql = "SELECT * FROM agenda"
cursor.execute(sql)
datos = cursor.fetchall()

def index(request):
	return HttpResponse("Version de base de datos: %s" % version)

def lista(request):
	return render('inicio.html',{'datos':datos})

def detalle(request, id):
	sql = "SELECT * FROM agenda WHERE id = %s"
	val = (id)
	cursor.execute(sql, val)
	dato = cursor.fetchall()
	return HttpResponse("Datos: %s" % dato)

def nuevo(request, nom, num, dirc):
	sql = "INSERT INTO agenda(nombre, telefono, direccion) values(%s, %s, %s)"
	val = (nom, num, dirc)
	cursor.execute(sql, val)

	db.commit()
	return HttpResponse("%s se agrego correctamente." % nom) 