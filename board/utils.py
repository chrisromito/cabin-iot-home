import itertools
from typing import Any, Iterable, List


def flatten(nested_list: Iterable[Any]) -> List[Any]:
    return list(
        itertools.chain.from_iterable(nested_list)
    )
