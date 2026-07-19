import json
import Student
import Student_marks
def add_student ():
    Student.COUNT+=1
    print("------TO ADD STUDENTS, PLEASE FILL THE DETAILS BELOW : ------------------------")
    roll = Student.COUNT
    name = input("PLEASE ENTER NAME OF STUDENT :")
    Age1 = int(input("PLEASE ENTER AGE OF STUDENT : "))
    class1 = input("PLEASE ENTER AGE OF STUDENT :")
    city = input("PLEASE ENTER THE CITY NAME : ")
    maths = int(input("ENTER MARKS OBTAINED IN Maths: "))
    phy = int(input("ENTER MARKS OBTAINED IN Physics: "))
    chem = int(input("ENTER MARKS OBTAINED IN Chemistry: "))
    eng = int(input("ENTER MARKS OBTAINED IN English: "))
    hindi = int(input("ENTER MARKS OBTAINED IN Hindi: "))
    # NOW ADDING THE STUDENT 
    Student.STUDENT["ROLL NO"][roll] = {"NAME": name,"AGE": Age1,"CLASS": class1,"CITY": city}
    Student_marks.MARKS["ROLL NO"][roll] = {"MATHS" : maths, "PHY" : phy, "CHEM" : chem, "ENG" : eng,"HINDI" : hindi}
    print("STUDENT ADDED SUCCESFULLY")


def view_student() :
    for roll in Student.STUDENT["ROLL NO"]:

        details = Student.STUDENT["ROLL NO"][roll]
        marks = Student_marks.MARKS["ROLL NO"][roll]

        print("\n----------------------------------------")
        print("ROLL NO :", roll)
        print("NAME    :", details["NAME"])
        print("AGE     :", details["AGE"])
        print("CLASS   :", details["CLASS"])
        print("CITY    :", details["CITY"])

        print("\nMARKS")
        print("Maths      :", marks["MATHS"])
        print("Physics    :", marks["PHY"])
        print("Chemistry  :", marks["CHEM"])
        print("English    :", marks["ENG"])
        print("Hindi      :", marks["HINDI"])
        print("----------------------------------------")

def search_student():
    rno = int(input("PLEASE ENTER THE ROLL NUMBER OF THE STUDENT TO BE SEARCHED : "))
    i = 0
    MARK = 0
    while i <= Student.COUNT:
        if rno == Student.STUDENT["ROLL NO"] :
            print("STUDENT FOUND SUCCESFULLY")  
            MARK = 1
        if MARK == 0 :
            print("STUDENT NOT FOUND")        

def update_student():
    print("----------SELECT THE TUPLE YOU WANT TO UPDATE : ------------------- ")
    print("\t\n 1)NAME\t\n 2)AGE \t\n 3)CLASS \t\n 4)CITY \t\n 5)SUBJECT MARKS")
    choice= int(input("PLEASE ENTER YOUR CHOICE : "))
    match choice : 
        case 1 : 
            try :
                r = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE NAME IS TO BE UPDATED : "))
                new = input("PLEASE ENTER THE NEW NAME OF THE STUDENT : ")
                Student.STUDENT["ROLL NO"][r]["NAME"] = new
                print("UPDATION COMPLETED SUCCESFULLY")

            except :
                print("PLEASE ENTER A VALID ROLL NO AND TRY AGAIN")
                update_student()
        case 2 : 
             try :
                r = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE AGE IS TO BE UPDATED : "))
                new1 = int(input("PLEASE ENTER THE AGE OF THE STUDENT : "))
                Student.STUDENT["ROLL NO"][r]["AGE"] = new1
                print("UPDATION COMPLETED SUCCESFULLY")
             except ValueError:
                 print("values are not int, PLEASE TRY AGAIN")
                 update_student()
             except :
                print("PLEASE ENTER A VALID ROLL NO AND TRY AGAIN")
                update_student()
        case 3 : 
            try :
                r = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE CLASS IS TO BE UPDATED : "))
                new2 = int(input("PLEASE ENTER NEW CLASS OF THE STUDENT : "))
                Student.STUDENT["ROLL NO"][r]["CLASS"] = new2
                print("UPDATION COMPLETED SUCCESFULLY")
            except ValueError:
                 print("values are not int, PLEASE TRY AGAIN")
                 update_student()
            except :
                print("PLEASE ENTER A VALID ROLL NO AND TRY AGAIN")
                update_student()
        case 4 : 
            try :
                r = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE CITY IS TO BE UPDATED : "))
                new3 = int(input("PLEASE ENTER THE RESIDING CITY OF THE STUDENT : "))
                Student.STUDENT["ROLL NO"][r]["CITY"] = new3
                print("UPDATION COMPLETED SUCCESFULLY")
            except ValueError:
                 print("values are not int, PLEASE TRY AGAIN")
                 update_student()
            except :
                print("PLEASE ENTER A VALID ROLL NO AND TRY AGAIN")
                update_student()
        case 5 :
            print("PLEASE SELECT THE SUBJECT WHERE MARKS NEED TO BE UPDATED : ")
            print("\t\n 1)MATH \t\n 2)PHY \t\n 3)CHEM \t\n 4)ENG \t\n 5)SUBJECT HINDI")
            ch = int(input('PLEASE ENTER YOUR CHOICE : '))
            if ch == 1 :
                sub = "MATHS"
            if ch == 2 :
                sub = "PHY"
            if ch == 3 :
                sub = "CHEM"
            if ch == 4 :
                sub = "ENG"
            if ch == 5 :
                sub = "HINDI"
            try :
                r = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE MARKS NEEDS IS TO BE UPDATED : "))
                new4 = int(input("PLEASE ENTER THE NEW MARKS OF THE STUDENT : "))
                Student_marks.MARKS["ROLL NO"][r][sub] = new4
                print("UPDATION COMPLETED SUCCESFULLY")
            except :
                print("PLEASE ENTER A VALID ROLL NO AND TRY AGAIN")
                update_student()
    
def del_student():
    try : 
        c = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT TO BE DELETED : "))
        con = input((f" ARE YOU SURE YOU WANT TO DELETE STUDENT {c} ? "))
        if c in Student.STUDENT["ROLL NO"] :
            if con == 'YES' or con == "yes" or con == "Y"or  con == "y" : 
                    del Student.STUDENT["ROLL NO"][c]
                    del Student_marks.MARKS["ROLL NO"][c]
                    print("STUDENT DELETED SUCCESFULLY")
            else : 
                print('PLEASE ENTER A VALID RESPONSE AND TRY AGAIN LATER !')
                del_student()
        else :
            print("NO SUCH STUDENT EXISTS !")
    except ValueError :
        print("PLEASE ENTER A VALID ROLL NO")

def calc_percentage():
    try: 
        c = int(input("PLEASE ENTER THE ROLL NO OF THE STUDENT WHOSE PERCENTAGE IS TO BE CALCULATED : "))
        if c in Student.STUDENT["ROLL NO"] :
            m = Student_marks.MARKS["ROLL NO"][c]["MATHS"]
            p = Student_marks.MARKS["ROLL NO"][c]["PHY"]
            che = Student_marks.MARKS["ROLL NO"][c]["CHEM"]
            e = Student_marks.MARKS["ROLL NO"][c]["HINDI"]
            h = Student_marks.MARKS["ROLL NO"][c]["ENG"]
            perct= (m+p+che+e+h)/500 *100
            print(f'TOTAL PERCENTAGE OBTAINED : {perct}')
            return perct
        else :
            print("NO SUCH STUDENT EXISTS !")
            return 0
    except ValueError :
        print("PLEASE ENTER A VALID ROLL NO ")
        return 0

def grade_evaluator ():
        t = float(calc_percentage())
        if t >= 90 :
            print("GRADE : A+")
        elif 80<= t <90 :
            print("GARDE : A")
        elif 70<= t <80:
            print("GRADE : B")
        elif 60<= t <70:
            print("GRADE : C")
        elif 50<= t <60:
            print("GRADE : D")
        else :
            print("GRADE : FAIL")

def subject_Topper():
     subjects = ["MATHS", "PHY", "CHEM", "ENG", "HINDI"]
     for subject in subjects:

        highest = -1
        topper_roll = 0

        for roll in Student_marks.MARKS["ROLL NO"]:

            marks = Student_marks.MARKS["ROLL NO"][roll][subject]

            if marks > highest:
                highest = marks
                topper_roll = roll

        name = Student.STUDENT["ROLL NO"][topper_roll]["NAME"]

        print("-------------------------------------")
        print("SUBJECT :", subject)
        print("TOPPER  :", name)
        print("ROLL NO :", topper_roll)
        print("MARKS   :", highest)
                    
def save_data():

    try:
        with open("student_data.json", "w") as file:
            json.dump(Student.STUDENT, file, indent=4)

        with open("marks_data.json", "w") as file:
            json.dump(Student_marks.MARKS, file, indent=4)

        print("DATA SAVED SUCCESSFULLY")

    except Exception as e:
        print("ERROR WHILE SAVING DATA :", e)

def read_data():
        try:

            with open("student_data.json", "r") as file:
                data = json.load(file)
            #typecasting
            Student.STUDENT["ROLL NO"] = {
                int(k): v for k, v in data["ROLL NO"].items()
            }

            with open("marks_data.json", "r") as file:
                data = json.load(file)
            #typecasting
            Student_marks.MARKS["ROLL NO"] = {
                int(k): v for k, v in data["ROLL NO"].items()
            }

            print("DATA READ SUCCESSFULLY\n")

            view_student()

        except FileNotFoundError:
            print("NO SAVED DATA FOUND.")

