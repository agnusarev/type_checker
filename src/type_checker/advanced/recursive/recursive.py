"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""

from typing import Dict, TypeAlias

Tree: TypeAlias = Dict[str, "Tree"]
