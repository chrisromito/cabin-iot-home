from typing import Dict
from db.connection import get_connection
from utils import flatten


def resident_is_home()-> bool:
    conn = get_connection()
    result = [
        row for row in
        conn.execute(
            '''
                select is_home from resident
                    where is_home = true
                    limit 1;
            '''
        )
    ]
    return bool(len(flatten(result)))


def write_component_status(component: str, status: Dict)-> None:
    conn = get_connection()
    conn.execute(
        '''insert into component_log (component, status) VALUES(?, ?)''',
        (component, json.dumps(status))
    )
