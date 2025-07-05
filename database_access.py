import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk
import customtkinter as ctk
import sqlite3
import random

# the window parent window
#create the connection with the database
connection = sqlite3.connect("student_data.db")
#create the cursor to give an access with the database
my_cursor = connection.cursor()
#creating the table for recording the student information
my_cursor.execute("""CREATE TABLE IF NOT EXISTS  students_record (
    First_name text,
    Last_name text,
    Username text,
    Mobile_no integer,
    Email text,
    Password integer,
    Gender text,
    Reg_no text)""") 
connection.commit()
#function to insert data into database
def insert_data(reiceved_data):
    # access with the list
    First_name = reiceved_data[0]
    Last_name = reiceved_data[1]
    Username = reiceved_data[2]
    Mobile_no = reiceved_data[3]
    Email = reiceved_data[4]
    Password = reiceved_data[5]
    comfirm = reiceved_data[6]
    Gender = reiceved_data[7]
    Reg_no = reiceved_data[8]
    #print('hello')
    if (
            First_name
            and
            Last_name
            and
            Username
            and
            Mobile_no
            and
            Email
            and
            Password
            and
            comfirm
            and
            Gender
            and
            Reg_no):
        if Password == comfirm :
            
            
    
            my_datalist = [
                First_name,
                Last_name,
                Username,
                Mobile_no,
                Email,
                Password,
                Gender,
                Reg_no]
            print(len(my_datalist))
            print(my_datalist)
            my_cursor.execute(" INSERT INTO students_record VALUES (?,?,?,?,?,?,?,?) ",my_datalist)
            my_cursor.execute("SELECT rowid, * FROM students_record")
            students = my_cursor.fetchall()
            connection.commit()
            print(students)

            msgbox.showinfo("Success","Details have been record successfully!")

            
        else:
            msgbox.showwarning('comfirmation','password mismatched!')
                        
    else:
        msgbox.showwarning('fill','fill in all the field')
#loading data from the database
def load_data():
    my_cursor.execute("SELECT rowid, *FROM students_record")
    data = my_cursor.fetchall()
    connection.commit()
    print(data)
#function to delete database stored data
def clea_data(id):
    my_cursor.execute("DELETE FROM students_record WHERE rowid = ? ",(id))
    connection.commit()
    print(my_cursor.fetchall())
#generating reg number function
def generate_reg_no():
    my_cursor.execute("SELECT rowid, *FROM students_record")
    data = my_cursor.fetchall()
    connection.commit()
    counter = len(data) + 1
    print(counter)
    
    reg_number = f"CAN/25/0{counter}"
    print(reg_number)
    return reg_number
generate_reg_no()

load_data()