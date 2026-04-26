# ***************************** 28/10/2025 *****************************
# information -- useful data is information
# data -- raw fact / everything is data
# database -- it a place or area where data store
# database management system (DBMS) -- it is a way to store data or manage data (software)

# ----------------------------- SQLite3 Database Operations -----------------------------
import sqlite3
# **** Connect to database (it will be created if not exists)
con = sqlite3.connect("my_database.db")
cursor = con.cursor()

# ----------------------------- Create Table -----------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS student(
    id INTEGER ,
    name TEXT,
    age INTEGER
)
''')
con.commit()
print("Table create successfully")

#----------------------------- Functions for CRUD (create , read , update , delete) Operations -----------------------------
id=23
name="ram"
age=22
cursor.execute("INSERT INTO student (id, name, age) VALUES (?, ?, ?)", (id, name, age))
cursor.execute("INSERT INTO student (id, name, age) VALUES (?, ?, ?)", (458, "ram", 241))

con.commit()
print("data insert successfully")

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print(rows)
for i in rows:
    print(i)

def insert_student():
    idd = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    cursor.execute("INSERT INTO student (id, name, age) VALUES (?, ?, ?)", (idd, name, age))
    con.commit()
    print("Record Inserted Successfully!\n")

def show_all_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n Student Records:")
    print("-" * 40)
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    print("-" * 40, "\n")

def search_student():
    idd = int(input("Enter ID to Search: "))
    cursor.execute("SELECT * FROM student WHERE id=?", (idd,))
    data = cursor.fetchone()
    if data:
        print(f"\n Found: ID={data[0]}, Name={data[1]}, Age={data[2]}\n")
    else:
        print("X No record found!\n")

def update_student():
    idd = int(input("Enter ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    cursor.execute("UPDATE student SET name=?, age=? WHERE id=?", (name, age, idd))
    con.commit()
    if cursor.rowcount > 0:
        print(" Record Updated Successfully!\n")
    else:
        print("X Record not found!\n")

def delete_student():
    idd = int(input("Enter ID to Delete: "))
    cursor.execute("DELETE FROM student WHERE id=?", (idd,))
    con.commit()
    if cursor.rowcount > 0:
        print(" Record Deleted Successfully!\n")
    else:
        print("X Record not found!\n")

# ------------------------- Main Menu -------------------------
while True:
    print("========= Student Database Menu =========")
    print("1. Insert Student")
    print("2. Show All Students")
    print("3. Search Student by ID")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        insert_student()
    elif choice == '2':
        show_all_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print(" Exiting... Thank you!")
        break
    else:
        print(" Invalid Choice! Please try again.\n")

# Close connection before exit
con.close()