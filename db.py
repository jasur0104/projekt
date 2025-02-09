import psycopg2

conn = psycopg2.connect(database='n47',
                        user='postgres',
                        password='jasur',
                        host='localhost',
                        port=5432
                        )

cur = conn.cursor()

create_users_table = """create table users_table(
    id serial primary key ,
    username varchar(100) not null unique ,
    password varchar(255) not null ,
    role varchar(20) not null ,
    status varchar(30) not null ,
    login_try_count int not null 
);
"""

create_todos_table = """create table todos_table(
    id serial PRIMARY KEY,
    name varchar(100) not null ,
    todo_type varchar(15) not null,
    user_id int references users(id)
);
"""


def create_table():
    cur.execute(create_users_table)
    cur.execute(create_todos_table)
    conn.commit()


def migrate():
    insert_into_users = """
    insert into users_table(username, password, role, status,login_try_count) 
    values ('admin','123','SUPERADMIN','ACTIVE',0);

    """
    cur.execute(insert_into_users)
    conn.commit()


def init():
    create_table()
    migrate()

if __name__ == '__main__':
    init()
