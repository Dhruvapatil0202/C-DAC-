
import sqlite3
import os

filepath = r"C:\Users\DAI.STUDENTSDC\Desktop\DAI 2024\Day18\user_database_temp.db"


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Successfully deleted: {file_path}")
        else:
            print(f"File does not exist: {file_path}")
    except Exception as e:
        print(f"Error occurred while deleting the file: {e}")
class Database_Interface:

    def __init__(self, filepath):
        self.filepath = filepath
        self.conn = sqlite3.connect(self.filepath)
        self.cursor = self.conn.cursor()

    def create_table(self, tablename):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {tablename}(
            userid INTEGER PRIMARY KEY,
            username TEXT,
            address TEXT,
            mobileno TEXT,
            email TEXT
            )
            """)

    def fetch_info(self, id):
        self.cursor.execute(f"""
        SELECT * FROM users WHERE id = {id}
        """)

        info = self.cursor.fetchall()
        return info if info else False

    def add_record(self, info):
        print(f"from username: {info}")

        self.cursor.execute(f"""
            INSERT INTO users (userid, username, address, mobileno, email)
            VALUES (?, ?, ?, ?, ?);
            """, info)

    def accept_input_from_user(self):
        id = int(input("Enter your ID: "))
        username = input("Enter your Username: ")
        address = input("Enter your address: ")
        mobile = input("Enter your mobile no.: ")
        email = input("Enter your email: ")

        return (id, username, address, mobile, email)

    def close_interface(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":

    delete_file(filepath)
    database_interface = Database_Interface(filepath)

    database_interface.create_table('users')


    database_interface.close_interface()