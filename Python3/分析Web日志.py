# -*- coding: utf-8 -*-
import re
import pymysql
from os import path
import time

db = {
    "host":"host",
    "user":"user",
    "password":"password",
    "db":"db",
    "charset":"utf8",
}

domain = "http://www.abc.com"

fileSize = path.getsize('1.log') 
log = open('1.log','r',encoding='UTF-8')
connection = pymysql.connect(host=db['host'], user=db['user'], password=db['password'],db=db['db'],charset=db['charset'])
sql = "INSERT INTO `history` (`ip`,`path`,`ua`,`referer`,`datetime`,`status`) VALUES (%s,%s,%s,%s,%s,%s)"
cur = 1;
with connection.cursor() as cursor:
    for line in log:
        print(cur)
        tmp = line.split(" ")
        if tmp[6].find(".js") > -1 or tmp[6].find(".css") > -1 or tmp[6].find(".ico") > -1:
            continue

        #ua
        ua = tmp[11:]
        ua = "".join(ua)
        ua = ua.replace("\n","")

        #time
        t = tmp[3]
        t = t[1:]
        timeArray = time.strptime(t, "%d/%b/%Y:%H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        o = {
            "ip":tmp[0],
            "path":domain + tmp[6],
            "status":tmp[8],
            "referer":tmp[10],
            "ua":ua,
            "datetime":str(timeStamp)
        }
        cursor.execute(sql, (o['ip'],o['path'],o['ua'],o['referer'],o['datetime'],o['status']))


connection.commit()
connection.close()
log.close()