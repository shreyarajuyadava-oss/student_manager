student = {}

while True:
    print("\n -------STUDENT MANAGER APP-------")
    print("1. Add Student")
    print("2. View Students")
    print("3. check result")
    print("4. Exit")

    choice = input("Enter your choice : ")

    #add student
    if choice == '1':
        name = input("Enter Student Name : ")
        marks = int(input("Enter Student Marks : "))
        student[name] = marks
        print(f"{name}added successfully!")

    #view student
    elif choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\nStudent List:")
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")

    #check result
    elif choice == '3':
        name = input("Enter Student Name to check result: ")
        if name in student:
            marks = student[name]
            if marks >= 50:
                print(f"{name} has passed with {marks} marks.")
            else:
                print(f"{name} has failed with {marks} marks.")
        else:
            print(f"No record found for student: {name}")

    #exit
    elif choice == '4':
        print("Exiting the Student Manager App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")