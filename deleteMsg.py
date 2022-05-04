#!/usr/bin/python3

# Names: Russell Rusnell and Lance Cagle
# Assignment: SY306 - Course Project

# Description: This program handles deleting messages from the message board.

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

def checkAdmin(dbconnection,login):
   user = login['username']
   mycursor = dbconnection.cursor()
   query = 'SELECT admin FROM user_table WHERE username="%s"'%(user)
   mycursor.execute(query)   
   row = mycursor.fetchone()
   return row[0]
   
def checkUser(dbconnection,login):
   currentMsgD = {}
   user = login['username']
   mycursor = dbconnection.cursor()
   query = 'SELECT msgID,username FROM msg_table'
   mycursor.execute(query)
   row = mycursor.fetchone()
   while row is not None:
      currentMsgD[row[0]] = row[1]
      row = mycursor.fetchone()
   print(currentMsgD)
   
   validIDs = []
   for k,v in currentMsgD.items():
      if v == user:
         validIDs.append(k)
   return validIDs
   
def deleteMsg(dbconnection):
   try:
      mycursor = dbconnection.cursor()
      query = 'DELETE FROM msg_table WHERE msgID="%s"'%(form["id"].value)
      mycursor.execute(query)
      row = mycursor.fetchone()
      dbconnection.commit()
      return
   except Exception as e:
      print(f"{e}: Unable to delete message")   
   


# Function Calls
# cookies = getCookies()
# Turns JSON sting into a dictionary
# login = json.loads(cookies["login"])
login = "test_user"
# Header information
# Includes style tags
print ("Content-type: text/html\n")  #REQUIRED

# Function Calls
dbconnection = connectDB()
adminStatus = checkAdmin(dbconnection,login)

if adminStatus == "false":
   print("NOT ADMIN")
   validIDs = checkUser(dbconnection,login)
else:
   print("ADMIN ACCESS")
   print("DELETING MESSAGE")
   deleteMsg(dbconnection)

print(validIDs)
if int(form['id'].value) in validIDs:
   print("MESSAGE ID VALID")
   print("DELETING MESSAGE")
   deleteMsg(dbconnection)
else:
   print("MESSAGE ID INVALID")
   