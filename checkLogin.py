#!/usr/bin/python3

# Names: Russell Rusnell and Lance Cagle
# Assignment: SY306 - Course Project

# Description: This program checks a users login information from a form against an SQL database. If the user is authenticated then the user is redirected to a member only page. If they user is not authenticated then they are denied access.

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
      
# Description: checks if a customer is in the user table
# Parameters: DBconnection object
# Return Types: DBconnection object
# Side Effects: 
#     checkPassword() is called if the user exists
#     program is exited if not
def checkLogin(dbconnection):
   currentUsers = []
   mycursor = dbconnection.cursor()
   query = 'SELECT username FROM user_table'
   mycursor.execute(query)
   row = mycursor.fetchone()
   while row is not None:
      currentUsers.append(row[0])
      row = mycursor.fetchone()
   
   if form['username'].value in currentUsers:
      print("USERNAME EXISTS")
      checkPassword(dbconnection)
   else:
      print(f"username: -- {form['username'].value} -- does not exist")
   return
   
# Description: checks if a customer has a correct password
# Parameters: DBconnection object
# Return Types: None
# Side Effects: 
def checkPassword(dbconnection):
   mycursor = dbconnection.cursor()
   query = 'SELECT password FROM user_table '
   query += 'WHERE username="%s"'%(form['username'].value)
   mycursor.execute(query)
   row = mycursor.fetchone()
   pWord = row[0]
   
   if form['password'].value == pWord:
      print("PASSWORDS MATCH")
      print("ALLOW ACCESS TO MEMEBR ONLY PAGE")
   
   else:
      print("INCORRECT PASSWORD")
   return

# Header information
# Includes style tags
print ("Content-type: text/html\n")  #REQUIRED


# Function Calls
dbconnection = connectDB()
checkLogin(dbconnection)
      
      
