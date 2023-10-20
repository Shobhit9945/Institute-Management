import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

user_data = pd.read_csv("users.csv")
sdf = pd.read_csv("students.csv")
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
            
      
        user = user_data[(user_data["Username"] == username) & (user_data["Password"] == password)]
        if not user.empty:
            print("Login successful.",f"Welcome {username}",sep="\n")
            break
        
        else:
            print("Invalid username or password. Please try again")

def main_menu():

    print("---------------------Welcome to Institute Management System---------------------")
    print("\n1. Login\n2. Exit")
    while True:
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            login()
            break
         
        elif choice == "2":
            print("Thank you for using the Institute Management System!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def add_student(sdf):
    
    if sdf.empty or sdf['SID'].isnull().all():
            sID = 1001
    else:
            sID = sdf['SID'].max() + 1
    
    name = input("Enter student's full name: ")
    dob=input("Enter student's date of birth: ")
    address = input("Enter student's address: ")
    phone = input("Enter student's phone number: ")
    email = input("Enter student's email address: ")
    enrollment_date = input("Enter student's enrollment date: ")
    course = input("Enter student's course: ")
    attendance=0
    GPA=0
    sdf.loc[len(sdf.index)] = [sID, name, dob, address, phone, email, enrollment_date, course, attendance, GPA]
    sdf.to_csv("student.csv", index=False)
    print("Student added successfully")



def main():
    main_menu()
    userinput=int(input("-------------------------------------------------------------------------\nStudents\t\tCourses\t\t\tFaculty\n\t\t\n1.Add Student Info\t6.Add Course\t\t11.Add Faculty\n2.Update Student Info\t7.Update Course\t\t12.Update Faculty Info\n3.Delete Student Info\t8.Delete Course\t\t13.Delete Faculty Info\n4.Search Student Info\t9.Show Course Info\t14.Search Faculty\n5.Student Report\t10.Course Report\n\n\t\t\t\t 15.Exit\n-------------------------------------------------------------------------\nTo use a particular command, type the number assigned to it\n=>"))
    if userinput==1:
         add_student(sdf)

    if userinput==15:
        print("Thank you for using the Institute Management System!")
        #exit()
#login(user_data)
main()