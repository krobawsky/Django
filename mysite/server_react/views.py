from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import pymysql
import collections

db = pymysql.connect('localhost', 'root', '', 'django')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def lista(request):

	sql = "SELECT * FROM producto"
	cursor.execute(sql)
	datos = cursor.fetchall()

	user_list = []
	for row in datos :
	    d = collections.OrderedDict()
	    d['codigo']  = row[0]
	    d['descripcion']   = row[1]
	    d['precio']      = row[2]
	    user_list.append(d)
	return JSONResponse(user_list)