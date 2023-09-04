database= {
    "students":[
        {"first_name":"Amo", "last_name":"Kuo", "Class": "3A"},
        {"first_name":"Winny", "last_name":"Chen", "Class": "3A"},
        {"first_name":"Teresa", "last_name":"Tao", "Class": "3B"},
    ],
    "teachers":[
        {"first_name":"Clare", "last_name":"Lin", "subject": "math", "Class": ["3A", "3B"]},
    ],
    "homeroom_teacher":[
        {"first_name":"Philip", "last_name":"Wang", "Class": "3A"},
    ]
}


def choose_path():
    while True:
        path = input("Choose a path (create, manage or end):").lower()
        if path == "create":
            user_type()
        elif path == "manage":
            manage()
        elif path =="end":
            print("End program.")
            break
        else:
            print("Invalid input!")

def user_type():
    user_type = input("Choose a user type (student, teacher, homeroom teacher or end):").lower()
    if user_type == "student":
        first_name = input("Provide first name:")
        last_name = input("Provide last name:")
        class_name = input("Provide class name:")

        database["students"].append(
            {"first_name": first_name, "last_name": last_name, "Class": class_name}
        )
    elif user_type == "teacher":
        first_name = input("Provide first name:")
        last_name = input("Provide last name:")
        subject_name = input("Provide subject name:")
        _classes = []
        while True:
            class_name = input("Provide class name:")
            if not class_name:
                break
            _classes.append(class_name)
        database["teachers"].append(
            {
                "first_name": first_name, 
                "last_name": last_name,
                "Class": _classes, 
                "subject":subject_name,
            }
        )

    elif user_type == "homeroom teacher":
        first_name = input("Provide first name:")
        last_name = input("Provide last name:")
        class_name = input("Provide class name:")

        database["homeroom teacher"].append(
            {"first_name": first_name, "last_name": last_name, "Class": class_name}
        )
    else:
        print("Invalid input!")
    

def manage():
    manage_type = input("Choose a manage type (class, student, teacher, homeroom teacher or end):").lower()
    #list all students in the class and the homeroom teacher.
    if manage_type == "class":
        class_name = input("Provide a class name:")
        for student in database["students"]:
            if student ["Class"] == class_name:
                print(student)
        for homeroom_teacher in database["homeroom_teacher"]:
            if homeroom_teacher ["Class"] == class_name:
                print(homeroom_teacher)
    # student: all the classes the student attends and the teachers of these classes
    if manage_type == "student":
        student_name = input("Provide a student name:")
        for student in database["students"]:
            if student ["last_name"] == student_name:
                class_name = student["Class"]
                print(student)
                for teacher in database["teachers"]:
                    if class_name in teacher ["Class"]:
                      print (teacher)
    # teacher: list all the classes the teacher teaches.
    if manage_type == "teacher":
        teacher_name = input("Provide a teacher name:")
        for teacher in database["teachers"]:
            if teacher ["last_name"] == teacher_name:
                classes = teacher["Class"]
                print(classes)
    # homeroom teacher list all students the homeroom teacher leads.
    if manage_type == "homeroom teacher":
        homeroomteacher_name = input("Provide a homeroom teacher name:")
        for homeroom_teacher in database["homeroom_teacher"]:
            if homeroom_teacher["last_name"] == homeroomteacher_name:
                class_name = homeroom_teacher["Class"]
                for student in database["students"]:
                    if student["Class"] == homeroom_teacher["Class"]:
                        print(student)
    else:
        print("Invalid input!")


choose_path()

