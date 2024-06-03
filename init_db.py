import mysql.connector


def init_db():
    db = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="root",
        database="data_catalog"
    )
    cursor = db.cursor()

    # Execute the SQL script
    with open('init_db.sql', 'r') as file:
        sql_script = file.read()

    cursor.execute(sql_script, multi=True)
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    init_db()
