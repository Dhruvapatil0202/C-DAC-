import sqlite3
conn = sqlite3.connect("Hands_on_2_student_data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS courses")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
grade TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
c_id INTEGER PRIMARY KEY,
c_name TEXT,
instructor TEXT
)
""")

print("tables created")

cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (1, 'name1', 23, 'A'))
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (2, 'name2', 24, 'B'))
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (3, 'name3', 25, 'C'))
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (4, 'name4', 26, 'B'))
cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (5, 'name5', 27, 'A'))

cursor.execute("INSERT INTO courses (c_id, c_name, instructor) VALUES (?, ?, ?)", (1, 'course1', 'abc'))
cursor.execute("INSERT INTO courses (c_id, c_name, instructor) VALUES (?, ?, ?)", (2, 'course2', 'xyz'))
cursor.execute("INSERT INTO courses (c_id, c_name, instructor) VALUES (?, ?, ?)", (3, 'course3', 'pqr'))
conn.commit()

cursor.execute("SELECT * FROM students WHERE grade = 'A'")
rows = cursor.fetchall()


cursor.execute("SELECT c_name, instructor FROM courses ORDER BY c_name")
rows = cursor.fetchall()



cursor.execute("UPDATE students SET name = 'Mayur', age = 24 WHERE id = 1")
cursor.execute("SELECT * FROM students WHERE id = 1")
row = cursor.fetchall()



cursor.execute("UPDATE courses SET instructor='Sam' WHERE c_id=2")
cursor.execute("SELECT * FROM courses")
row = cursor.fetchall()


cursor.execute("DELETE FROM students WHERE id = 3")
cursor.execute("SELECT * FROM students")
cursor.fetchall()

cursor.execute("DROP TABLE IF EXISTS courses")
cursor.execute("DROP TABLE IF EXISTS students")