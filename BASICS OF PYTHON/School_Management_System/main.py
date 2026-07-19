import definitions

USERNAME = "admin"
PASSWORD = "python123"

attempt = 0

while attempt < 3:

    username = input("ENTER USERNAME : ").strip()
    password = input("ENTER PASSWORD : ").strip()

    if username == USERNAME and password == PASSWORD:
        print("\nLOGIN SUCCESSFUL")
        break

    else:
        attempt += 1
        print(f"INVALID USERNAME OR PASSWORD ({attempt}/3)\n")

if attempt == 3:
    print("TOO MANY FAILED ATTEMPTS")
    exit()


while True:

    print("\n====================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Percentage")
    print("7. Grade")
    print("8. Subject Topper")
    print("9. Save Data")
    print("10. Read Data")
    print("11. Exit")
    print("====================================")

    try:
        choice = int(input("ENTER YOUR CHOICE : "))

        if choice == 1:
            definitions.add_student()

        elif choice == 2:
            definitions.view_student()

        elif choice == 3:
            definitions.search_student()

        elif choice == 4:
            definitions.update_student()

        elif choice == 5:
            definitions.del_student()

        elif choice == 6:
            definitions.calc_percentage()

        elif choice == 7:
            definitions.grade_evaluator()

        elif choice == 8:
            definitions.subject_Topper()

        elif choice == 9:
            definitions.save_data()

        elif choice == 10:
            definitions.read_data()

        elif choice == 11:
            print("\nTHANK YOU FOR USING STUDENT MANAGEMENT SYSTEM")
            break

        else:
            print("PLEASE ENTER A VALID CHOICE.")

    except ValueError:
        print("PLEASE ENTER A NUMBER ONLY.")