import pyodbc
import pymssql

server = 'sql5108.site4now.net'
database = 'db_a79b5b_proj13'
username = 'db_a79b5b_proj13_admin'
password = 'XXNEA6q6VbvATG6g'


def Connect_to_SQL_Server():
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return cnxn.cursor()


def Connect_to_SQL_Server_Pymssql():
    conn = pymssql.connect(server='sql5108.site4now.net',
                           user='db_a79b5b_proj13_admin', password='XXNEA6q6VbvATG6g', database='db_a79b5b_proj13')
    cursor = conn.cursor(as_dict=True)
    return cursor


if __name__ == '__main__':
    Connect_to_SQL_Server()
