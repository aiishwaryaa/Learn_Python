import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student(name TEXT, marks INTEGER)")
cursor.execute("INSERT INTO student VALUES('aishwarya',98)")
conn.commit()
conn.close()