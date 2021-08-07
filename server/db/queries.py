from typing import Dict
import operator
from functools import reduce

from db.connection import get_connection
from utils import flatten


def resident_is_home() -> bool:
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
    try:
        return bool(
            reduce(operator.__and__, flatten(result))
        )
    except TypeError:
        return False


def write_component_status(component: str, status: Dict) -> None:
    conn = get_connection()
    conn.execute(
        '''insert into component_log (component, status) VALUES(?, ?)''',
        (component, json.dumps(status))
    )


def update_home_status(is_home: bool):
    conn = get_connection()
    conn.execute(
        '''update resident set is_home = ?''',
        (is_home,)
    )
    return is_home
