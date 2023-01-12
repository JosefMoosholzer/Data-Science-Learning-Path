from typing import List, Dict, Optional, Callable
values: List[int] = []
counts: Dict[str, int] = {"libaries": 1, "imports": 4}
optional_arg: Optional[float] = None

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s,2)

def comma_repeater(s: str, n: int) -> str:
    return ", ".join([s for _ in range(n)])

assert twice(comma_repeater, "type annotation") == "type annotation, type annotations", "HEY"