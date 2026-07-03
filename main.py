import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="273208", 
    database="student_db"
)

cursor = conn.cursor()


# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    email = input("Enter email: ")

    sql = "INSERT INTO students (name, age, course, email) VALUES (%s, %s, %s, %s)"
    values = (name, age, course, email)

    cursor.execute(sql, values)
    conn.commit()
    print("Student added successfully!")


# ---------------- VIEW STUDENTS ----------------
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n--- STUDENT LIST ---")
    for row in rows:
        print(row)


# ---------------- SEARCH STUDENT ----------------
def search_student():
    sid = input("Enter student ID: ")

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("Student not found!")


# ---------------- UPDATE STUDENT ----------------
def update_student():
    sid = input("Enter student ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    course = input("New course: ")
    email = input("New email: ")

    sql = """
    UPDATE students 
    SET name=%s, age=%s, course=%s, email=%s 
    WHERE id=%s
    """

    values = (name, age, course, email, sid)

    cursor.execute(sql, values)
    conn.commit()

    print("Student updated successfully!")


# ---------------- DELETE STUDENT ----------------
def delete_student():
    sid = input("Enter student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()

    print("Student deleted successfully!")


# ---------------- MENU ----------------
while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")

conn.close()