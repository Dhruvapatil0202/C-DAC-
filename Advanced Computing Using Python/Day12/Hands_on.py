import sqlite3



def create_tables(cursor, conn):
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
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        instructor TEXT
        )
        """)
def insert(cursor, conn):
    cursor.execute("INSERT INTO courses (course_name,instructor) VALUES ('Python', 'xyz')")
    cursor.execute("INSERT INTO courses (course_name,instructor) VALUES ('Maths', 'pqr')")
    cursor.execute("INSERT INTO courses (course_name,instructor) VALUES ('AI', 'std')")

    cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (1, 'name1', 19, 'A'))
    cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (2, 'name2', 25, 'B'))
    cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (3, 'name3', 23, 'C'))
    cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (4, 'name4', 34, 'B'))
    cursor.execute("INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)", (5, 'name5', 32, 'A'))

    conn.commit()
def query(cursor, conn):

    cursor.execute("""
    SELECT * FROM students WHERE grade = A;
    """)
    print("All A grade students: \n")
    rows = cursor.fetchall()
    for row in rows: print(row)

    cursor.execute("SELECT * FROM courses ORDER BY course_name")
    print("ALL courses :")
    rows = cursor.fetchall()
    for row in rows: print(row)


if __name__ == "__main__":
    conn = sqlite3.connect("Hands_on_1_SchoolDB.db")
    cursor = conn.cursor()

    # create_tables(cursor, conn)

    # insert(cursor, conn)
    query(cursor, conn)


    cursor.close()
    conn.close()
