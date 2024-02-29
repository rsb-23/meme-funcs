"""
Bitbool shows the similarity and difference of Boolean and Bitwise operators.
 - Can be a good interview question.

** Rhymes with pitbull 😜
"""

from itertools import product


def bitbool(idx):
    ops = ["&", "|", "and", "or"]
    vals = [0, 1, False, True]

    for i, tups in enumerate(product(vals, ops, vals)):
        x = "{} {} {}".format(*tups)
        if i == idx:
            print(f"{x=}, val={eval(x)}")
            break
    else:
        print("ROFL")


if __name__ == "__main__":
    for ix in 32, 33, 40, 61, 64:
        bitbool(ix)
