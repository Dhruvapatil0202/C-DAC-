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