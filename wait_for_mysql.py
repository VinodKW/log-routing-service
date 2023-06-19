import time
import mysql.connector

def wait_for_mysql():
    while True:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='vinod',
                password='abcd',
                database='logdb',
            )
            conn.close()
            break
        except mysql.connector.Error:
            print('MySQL server is unavailable, waiting...')
            time.sleep(1)

if __name__ == '__main__':
    wait_for_mysql()
