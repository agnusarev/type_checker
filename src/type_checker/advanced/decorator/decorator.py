"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""

from typing import Callable, TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


def decorator(message: str) -> Callable:
    def inner(func: F) -> F:
        return func

    return inner
