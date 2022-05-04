#!/usr/bin/python3

# Names: Russell Rusnell and Lance Cagle
# Assignment: SY306 - Course Project

# Description: This program adds users to the user_table in the SQL database using information entered in a form on the sign-up html page.

import cgi
import json
import mysql.connector

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

# Description: adds a user to the user_table in the database
# Parameters: DBconnection object
# Return Types: 
# Side Effects: user added to user_table
def addUser(dbconnection):
   try:
      mycursor = dbconnection.cursor()
      query = 'INSERT INTO user_table (username,name,password) '
      query += 'VALUES ("%s","%s","%s")'%(form['username'].value,form['name'].value,form['password'].value)
      mycursor.execute(query)
      row = mycursor.fetchone()
      dbconnection.commit()
      return
   except Exception as e:
      print(f"{e}: Unable to add user to user_table")
      exit()
      
# Header information
# Includes style tags
print ("Content-type: text/html\n")  #REQUIRED

# Function Calls
dbconnection = connectDB()   
addUser(dbconnection)

print("USER ADDED")
print("""
   <!doctype html><title>Form Submitted</title>
   <head>
   <meta http-equiv="refresh" content="5;url=./../index.html" /> 
   </html>
   <body>
""")
