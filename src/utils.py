from typing import Callable, Any


def iife(func: Callable) -> Any:
    return func()
