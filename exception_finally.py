import sqlite3

conn = None
cursor = None

try:
    conn = sqlite3.connect('DATO/wombat.db')
except sqlite3.OperationalError as err:
    print("Sorry,", err)
    exit()  # exit program immediately
else:
    cursor = conn.cursor()
    cursor.execute('select 123')
    result = cursor.fetchone()
    print(result)
finally:
    if conn is not None:
        conn.close()