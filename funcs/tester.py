from typing import Callable


def tester(func: Callable, expectations: dict):
    for inp, outp in expectations.items():
        assert func(inp) == outp, func(inp)
