import sqlite3 
DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)
# add records to the courses table
# courses = [
#     (351, "JavaScript course", 451, 100),
#     (614, "C++ course", 161, 10),
#     (721, "Java full course", 100, 35)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

# create file db
# with sqlite3.connect(DB_NAME) as sqlite_conn: 
#     print(sqlite_conn)
#     print(sqlite3.version_info)

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses(
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)