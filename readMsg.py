#!/usr/bin/python3

# Names: Russell Rusnell and Lance Cagle
# Assignment: SY306 - Course Project

# Description: This program handles reading the message board.

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
      
# Description: reads the msg_table and retuns the json object
# Parameters: DBconnection object
# Return Types: None
# Side Effects: msg_table returned as a JSON object, to be called by script
def readMsg(dbconnection):
   msgs = {}
   mycursor = dbconnection.cursor()
   query = "SELECT * FROM msg_table"
   mycursor.execute(query)
   row = mycursor.fetchone()
   
   while row is not None:
      oneMsgD = {"id":row[0],"message":row[1],"username":row[2],"time":row[3]}
      
      msgs[row[0]] = oneMsgD
      
      row = mycursor.fetchone()
   print(json.dumps(msgs,default=str))
      
# Header information
# Includes style tags
print ("Content-type: text/html\n")  #REQUIRED

# Function Calls
dbconnection = connectDB()
readMsg(dbconnection)