import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
user_data = pd.read_csv("users.csv")
sdf = pd.read_csv("students.csv")
cdf = pd.read_csv("courses.csv")
fdf = pd.read_csv("faculty.csv")


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

#Student
def add_student(sdf):
    
    if sdf.empty:
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
    sdf.to_csv("students.csv", index=False)
    print("Student added successfully")

def update_student(sdf):
    print("Update Student Info")
    sID = int(input("Enter student's ID: "))
    student = sdf[sdf["SID"] == sID]
    if student.empty:
        print("Student not found")
        return
    print("Student found")
    print(student)
    print("Select the field you want to update")
    print("1. Name\n2. Date of Birth\n3. Address\n4. Phone\n5. Email\n6. Enrollment Date\n7. Course\n8. Attendance\n9. GPA")
    choice = int(input("Enter your choice (1-9): "))
    if choice == 1:
        name = input("Enter student's new name: ")
        sdf.loc[sdf["SID"] == sID, "Name"] = name
    elif choice == 2:
        dob = input("Enter student's new date of birth: ")
        sdf.loc[sdf["SID"] == sID, "Date of Birth"] = dob
    elif choice == 3:
        address = input("Enter student's new address: ")
        sdf.loc[sdf["SID"] == sID, "Address"] = address
    elif choice == 4:
        phone = input("Enter student's new phone number: ")
        sdf.loc[sdf["SID"] == sID, "Phone"] = phone
    elif choice == 5:
        email = input("Enter student's new email address: ")
        sdf.loc[sdf["SID"] == sID, "Email"] = email
    elif choice == 6:
        enrollment_date = input("Enter student's new enrollment date: ")
        sdf.loc[sdf["SID"] == sID, "Enrollment Date"] = enrollment_date
        
    elif choice == 7:
        course = input("Enter student's new course: ")
        sdf.loc[sdf["SID"] == sID, "Course"] = course

    elif choice == 8:
        attendance = input("Enter student's new attendance: ")
        sdf.loc[sdf["SID"] == sID, "Attendance"] = attendance
    
    elif choice == 9:
        GPA = input("Enter student's new GPA: ")
        sdf.loc[sdf["SID"] == sID, "GPA"] = GPA
    
    else:
        print("Invalid choice. Please try again.")

    sdf.to_csv("students.csv", index=False)
    print("Student updated successfully")     


def delete_student(sdf):
    print("Delete Student Info")
    sID = int(input("Enter student's ID: "))
    student = sdf[sdf["SID"] == sID]
    if student.empty:
        print("Student not found")
        return
    print("Student found")
    print(student)
    choice = input("Are you sure you want to delete this student? (Y/N): ")
    if choice == "Y":
        sdf = sdf[sdf["SID"] != sID]
        sdf.to_csv("students.csv", index=False)
        print("Student deleted successfully")
    else:
        print("Student not deleted")

def search_student(sdf):
    print("Search Student Info")
    option=int(input("1. Search by Name\n2. Search by ID\nEnter your choice (1-2): "))
    if option == 1:
        name = input("Enter student's name: ")
        student = sdf[sdf["Name"] == name]
        if student.empty:
            print("Student not found")
            return
        print("Student found")
        print(student)
    elif option == 2:

        sID = int(input("Enter student's ID: "))
        student = sdf[sdf["SID"] == sID]
        if student.empty:
            print("Student not found")
            return
        print("Student found")
        print(student)
    else:
        print("Invalid choice. Please try again.")

def student_report(sdf):
    choice=int(input("Student reports available:\n1. Attendance\n2. GPA\nEnter your choice (1-2): "))
    if choice == 1:
        student_attendance(sdf)
    elif choice == 2:
        student_gpa(sdf)
        
    else:
        print("Invalid choice. Please try again.")

def student_attendance(sdf):
    plt.bar(sdf["Name"], sdf["Attendance"])
    plt.xlabel("Name")
    plt.ylabel("Attendance")
    plt.title("Student Report")
    plt.show()

def student_gpa(sdf):
    plt.bar(sdf["Name"], sdf["GPA"])
    plt.xlabel("Name")
    plt.ylabel("GPA")
    plt.title("Student Report")
    plt.show()

#Course
def add_course(cdf):
                      
    if cdf.empty:
        cID = 1001
    else:
        cID = cdf['CID'].max() + 1
        
    name = input("Enter course name: ")
    faculty = input("Enter course faculty: ")
    credits = input("Enter course credits: ")
    seats = input("Enter course seats: ")
    duration=input("Enter course duration: ")
    fees = input("Enter course fees: ")
    cdf.loc[len(cdf.index)] = [cID, name, faculty, credits, seats, duration, fees]
    cdf.to_csv("courses.csv", index=False)
    print("Course added successfully")

def update_course(cdf):
    cid = int(input("Enter course ID: "))
    course = cdf[cdf["CID"] == cid]
    if course.empty:
        print("Course not found")
        return
    print("Course found")
    print(course)
    print("Select the field you want to update")
    choice =int(input("1. Name\n2. Faculty\n3. Credits\n4. Seats\n5. Duration\n6. Fees\nEnter your choice (1-6): "))
    if choice == 1:
        name = input("Enter course's new name: ")
        cdf.loc[cdf["CID"] == cid, "Name"] = name
    elif choice == 2:
        faculty = input("Enter course's new faculty: ")
        cdf.loc[cdf["CID"] == cid, "Faculty"] = faculty
    elif choice == 3:
        credits = input("Enter course's new credits: ")
        cdf.loc[cdf["CID"] == cid, "Credits"] = credits
    elif choice == 4:
        seats = input("Enter course's new seats: ")
        cdf.loc[cdf["CID"] == cid, "Seats"] = seats
    elif choice == 5:
        duration = input("Enter course's new duration: ")
        cdf.loc[cdf["CID"] == cid, "Duration"] = duration
    elif choice == 6:
        fees = input("Enter course's new fees: ")
        cdf.loc[cdf["CID"] == cid, "Fees"] = fees
    else:
        print("Invalid choice. Please try again.")

    cdf.to_csv("courses.csv", index=False)
    print("Course updated successfully")


def delete_course(cdf):
    print("Delete Course Info")
    cid = int(input("Enter course ID: "))
    course = cdf[cdf["CID"] == cid]
    if course.empty:
        print("Course not found")
        return
    print("Course found")
    print(course)
    choice = input("Are you sure you want to delete this course? (Y/N): ")
    if choice == "Y":
        cdf = cdf[cdf["CID"] != cid]
        cdf.to_csv("courses.csv", index=False)
        print("Course deleted successfully")
    else:
        print("Course not deleted")

def search_course(cdf):
    print("Search Course Info")
    option=int(input("1. Search by Course Name\n2. Search by Course ID\nEnter your choice (1-2): "))

    if option == 1:
        name = input("Enter course name: ")
        course = cdf[cdf["CNAME"] == name]
        if course.empty:
            print("Course not found")
            return
        print("Course found")
        print(course)
    elif option == 2:
        
        cid = int(input("Enter course ID: "))
        course = cdf[cdf["CID"] == cid]
        if course.empty:
            print("Course not found")
            return
        print("Course found")
        print(course)

    else:
        print("Invalid choice. Please try again.")

def course_report(cdf):
    choice=int(input("Course reports available:\n1. Seats\n2. Fees\nEnter your choice (1-2): "))
    if choice == 1:
        course_seats(cdf)
    elif choice == 2:
        course_fees(cdf)
    else:
        print("Invalid choice. Please try again.")

def course_seats(cdf):
    plt.bar(cdf["Name"], cdf["Seats"])
    plt.xlabel("Name")
    plt.ylabel("Seats")
    plt.title("Course Report")
    plt.show()

def course_fees(cdf):
    plt.bar(cdf["CNAME"], cdf["Fees"])
    plt.xlabel("Course Name")
    plt.ylabel("Fees Per Annum")
    plt.title("Course Report")
    plt.show()

#Faculty
def add_faculty(fdf):
    if fdf.empty:
        fID = 1001
    else:
        fID = fdf['FID'].max() + 1
        
    name = input("Enter faculty name: ")
    course = input("Enter faculty course: ")
    join_date = input("Enter faculty join date: ")
    salary = input("Enter faculty salary: ")
    address = input("Enter faculty address: ")
    phone = input("Enter faculty phone number: ")
    email = input("Enter faculty email address: ")
    
    fdf.loc[len(fdf.index)] = [fID, name, course, join_date, salary, address, phone, email]
    fdf.to_csv("faculty.csv", index=False)
    print("Faculty added successfully")

def update_faculty(fdf):
    fid = int(input("Enter faculty ID: "))
    faculty = fdf[fdf["FID"] == fid]
    if faculty.empty:
        print("Faculty not found")
        return
    print("Faculty found")
    print(faculty)
    print("Select the field you want to update")
    choice =int(input("1. Name\n2. Course\n3. Join Date\n4. Salary\n5. Address\n6. Phone\n7. Email\nEnter your choice (1-7): "))
    if choice == 1:
        name = input("Enter faculty's new name: ")
        fdf.loc[fdf["FID"] == fid, "Name"] = name
    elif choice == 2:
        course = input("Enter faculty's new course: ")
        fdf.loc[fdf["FID"] == fid, "Course"] = course
    elif choice == 3:
        join_date = input("Enter faculty's new join date: ")
        fdf.loc[fdf["FID"] == fid, "Join Date"] = join_date
    elif choice == 4:
        salary = input("Enter faculty's new salary: ")
        fdf.loc[fdf["FID"] == fid, "Salary"] = salary
    elif choice == 5:
        address = input("Enter faculty's new address: ")
        fdf.loc[fdf["FID"] == fid, "Address"] = address
    elif choice == 6:
        phone = input("Enter faculty's new phone number: ")
        fdf.loc[fdf["FID"] == fid, "Phone"] = phone
    elif choice == 7:
        email = input("Enter faculty's new email address: ")
        fdf.loc[fdf["FID"] == fid, "Email"] = email
    else:
        print("Invalid choice. Please try again.")

    fdf.to_csv("faculty.csv", index=False)
    print("Faculty updated successfully")

def delete_faculty(fdf):
    print("Delete Faculty Info")
    fid = int(input("Enter faculty ID: "))
    faculty = fdf[fdf["FID"] == fid]
    if faculty.empty:
        print("Faculty not found")
        return
    print("Faculty found")
    print(faculty)
    choice = input("Are you sure you want to delete this faculty? (Y/N): ")
    if choice == "Y":
        fdf = fdf[fdf["FID"] != fid]
        fdf.to_csv("faculty.csv", index=False)
        print("Faculty deleted successfully")
    else:
        print("Faculty not deleted")

def search_faculty(fdf):
    print("Search Faculty Info")
    option=int(input("1. Search by Faculty Name\n2. Search by Faculty ID\nEnter your choice (1-2): "))
    if option == 1:
        name = input("Enter faculty name: ")
        faculty = fdf[fdf["Name"] == name]
        if faculty.empty:
            print("Faculty not found")
            return
        print("Faculty found")
        print(faculty)
    elif option == 2:
        fid = int(input("Enter faculty ID: "))
        faculty = fdf[fdf["EID"] == fid]
        if faculty.empty:
            print("Faculty not found")
            return
        print("Faculty found")
        print(faculty)
    else:
        print("Invalid choice. Please try again.")



def faculty_report(fdf):
    choice=int(input("Faculty reports available:\n1. Years of Service\n2. Salary Report\nEnter your choice (1): "))
    if choice == 1:
        faculty_years_of_service(fdf)
    
    elif choice ==2:
        hindex=fdf['Salary'].idxmax()
        lindex=fdf['Salary'].idxmin()
        print("\nSalary Report\n")
        print(f"HIGHEST PAID FACULTY\n {fdf.at[hindex, 'Name']} {fdf.at[hindex, 'Salary']}")
        print(f"\nLOWEST PAID FACULTY\n {fdf.at[lindex, 'Name']} {fdf.at[lindex, 'Salary']}")
        print(f"\nThe average salary of all faculty is {fdf['Salary'].mean()}")


    else:
        print("Invalid choice. Please try again.")

def faculty_years_of_service(fdf):
    fdf['JoinDate'] = pd.to_datetime(fdf['JoinDate'])
    current_year = datetime.now().year
    #fdf['Years of Service'] = 
    plt.bar(fdf['Name'],current_year - fdf['JoinDate'].dt.year)
    plt.xlabel("Faculty Name")
    plt.ylabel("Years of Service")
    plt.title("Faculty Years of Service")
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.show()

def main():
    main_menu()
    while True:
        
        userinput=input("-------------------------------------------------------------------------\nStudents\t\tCourses\t\t\tFaculty\n\t\t\n1.Add Student Info\t6.Add Course\t\t11.Add Faculty\n2.Update Student Info\t7.Update Course\t\t12.Update Faculty Info\n3.Delete Student Info\t8.Delete Course\t\t13.Delete Faculty Info\n4.Search Student Info\t9.Show Course Info\t14.Search Faculty\n5.Student Report\t10.Course Report\t15.Faculty Report\n\n\t\t\t\t 16.Exit\n-------------------------------------------------------------------------\nTo use a particular command, type the number assigned to it\n=>")
        
        #Students
        if userinput=="1":
            add_student(sdf)

        elif userinput=="2":
            update_student(sdf)

        elif userinput=="3":
            delete_student(sdf)
        
        elif userinput=="4":
            search_student(sdf)

        elif userinput=="5":
            student_report(sdf)

        #Courses

        elif userinput=="6":
            add_course(cdf)

        elif userinput=="7":
            update_course(cdf)

        elif userinput=="8":
            delete_course(cdf)

        elif userinput=="9":
            search_course(cdf)
        
        elif userinput=="10":
            course_report(cdf)

        #Faculty
        elif userinput=="11":
            add_faculty(fdf)
        
        elif userinput=="12":
            update_faculty(fdf)

        elif userinput=="13":
            delete_faculty(fdf)

        elif userinput=="14":
            search_faculty(fdf)

        elif userinput=="15":
            faculty_report(fdf)

        elif userinput=="16":
            print("Thank you for using the Institute Management System!")
            break

        else:
            print("Invalid choice. Please try again.")
        #exit()
#login(user_data)
main()