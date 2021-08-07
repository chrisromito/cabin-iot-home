from db.connection import get_connection


def create():
    print('Setting up DB tables...')
    conn = get_connection()
    try:
        cursor = conn.cursor()
        create_resident_table(conn, cursor)
        create_component_log_table(conn, cursor)
    except Exception as err:
        print('Caught an error whilst trying to create tables')
        print(err)
        raise err
    finally:
        conn.close()


def create_resident_table(conn, cursor):
    print('Creating resident table...')
    cursor.execute('''
        create table resident (
            id integer not null primary key,
            first_name varchar not null,
            last_name varchar not null,
            is_home bool not null default false
        )
    ''')
    cursor.execute('''insert into resident VALUES(1, 'Chris', 'Romito', false )''')
    conn.commit()
    print('resident table was created')


def create_component_log_table(conn, cursor):
    print('Creating component_log table...')
    cursor.execute('''
        create table component_log(
            id integer not null primary key,
            component varchar not null,
            status text not null,
            created_at timestamp default (datetime('now', 'localtime'))
        );
    ''')
    conn.commit()
    print('component_log table was created')
