from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from dotenv import load_dotenv
import mysql.connector
import os
import setting 
import json
load_dotenv()

MYSQL_HOST=os.getenv("mysql_host")
MYSQL_PORT=os.getenv("mysql_port")
MYSQL_USER=os.getenv("mysql_user")
MYSQL_PASSWORD=os.getenv("mysql_password")



connection = mysql.connector.connect(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,password=MYSQL_PASSWORD)
cursor = connection.cursor()
cursor.execute("USE `webside`")
# cursor.execute("SELECT `id`,`name`,`username` FROM `member` WHERE `username` = 'lin' " )
cursor.execute("SELECT JSON_OBJECT('id',`id`,'name',`name`,'username',`username`) FROM `member` WHERE `username` = 'lin'")
results=cursor.fetchall()
# respone = json.dumps(results,ensure_ascii=False)

print(results)