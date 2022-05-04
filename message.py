#!/usr/bin/python3

# Names: Russell Rusnell and Lance Cagle
# Assignment: SY306 - Course Project

# Description: This program handles the message board database.

import cgi
import json
import mysql.connector
import os

# Global Variables
HOST = "localhost"
USER = "russ"
PASS = "NinjaCookie57!!"
DB = "Project"

# Login Form from HTML Page
form = cgi.FieldStorage()

# Description: creates a connection to the database
# Parameters: None
# Return Types: DBconnection object
# Side Effects: connection created between program and database
def connectDB():
   try:
      mydb = mysql.connector.connect(
         host=HOST,
         user=USER,
         password=PASS,
         database=DB,
         auth_plugin='mysql_native_password'
      )
      return (mydb)
   except Exception as e:
      print(f"{e}: Unable to connect to database")

# Description: Parses the cookie information from the server
# Parameters: None
# Return Types: Dictionary
# Side Effects: None
def getCookies():
    if 'HTTP_COOKIE' in os.environ:
        cookie_string=os.environ.get('HTTP_COOKIE')
        
        #parse the cookies received into a dictionary
        parseCookie= cookie_string.split(';')
        cookies = {}

        for item in parseCookie:
            if len(item.strip()) == 0:
              continue
            split=item.split('=')
            cookies[split[0].strip()] = split[1].strip()
        return cookies
    else:
      return {}
      
def addMsg(dbconnection,login):
   print("In add message")
   print(login)
   
   mycursor = dbconnection.cursor()
   query = 'INSERT INTO msg_table (username,msg) '
   query += 'VALUES ("%s","%s")'%(login,form['message'].value)
   print(query)
   mycursor.execute(query)
   row = mycursor.fetchone()
   dbconnection.commit()
   return
   # except Exception as e:
   #    print(f"{e}: Unable to add message to message table")
   
# Function Calls
cookies = getCookies()
# Turns JSON sting into a dictionary
login = json.loads(cookies["login"])

# Header information
# Includes style tags
print ("Content-type: text/html\n")  #REQUIRED

# Function Calls
dbconnection = connectDB()
addMsg(dbconnection,login)   

print("""
   <!doctype html><title>Form Submitted</title>
   <head>
   <meta http-equiv="refresh" content="2;url=./../members.html" /> 
   </html>
   <body>
""")     
