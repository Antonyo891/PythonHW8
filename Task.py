import sqlite3 as sl

def create_table():
#создаем пустую таблицу users со столбцами id, name, age если ее не было в БД
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )""")
    con.commit()  # сохраняем изменения


def add_into_empty():  #если таблица пустая то добавляется 2 записи
    cur.execute("select * from users")
    if not cur.fetchall():
        cur.execute("INSERT INTO users (name,age) VALUES ('Иванов', 30)")
        con.commit()
        cur.execute("INSERT INTO users (name,age) VALUES ('Петров', 33)")
        con.commit()

def show_data(): # показываем все записи таблицы users
    cur.execute("select * from users")
    for row in cur.fetchall():
        print(row)

con = sl.connect("gb.db")   # соединяемся с БД , если ее нету, то создаем такую БД

cur = con.cursor()        # создаем указатель , через него будем выполнять запросы


create_table()
add_into_empty()
show_data()