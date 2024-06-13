"""
TODO:

`make_object` takes a class returns an instance of it.
"""

from typing import TypeVar, Type

T = TypeVar("T")


def make_object(cls: Type[T]) -> T:
    return cls()
