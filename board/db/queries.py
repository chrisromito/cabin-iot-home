from typing import Dict
from db.connection import get_connection


def write_component_status(component: str, status: Dict) -> None:
    conn = get_connection()
    conn.execute(
        '''insert into component_log (component, status) VALUES(?, ?)''',
        (component, json.dumps(status))
    )
