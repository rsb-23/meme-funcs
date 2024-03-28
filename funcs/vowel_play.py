import re
from typing import Callable


def vowel_index(word: str) -> int:
    """Returns index of 1st vowel in a word"""
    vowels = r"[aeiouyAEIOU@03]"
    return re.search(vowels, word.title()).span()[0]


def akshay_swap(phrase: str) -> str:
    """Swaps consonant prefixes of 1st and last word in 2/3 word phrase"""
    words = phrase.split()
    n_words = len(words)
    if n_words == 2:
        first, last = words
        mid = " "
    elif n_words == 3:
        first, mid, last = words
        mid = f" {mid} "
    else:
        return "You are MEME illiterate"

    try:
        a, b = vowel_index(first), vowel_index(last)
    except AttributeError:
        return " ".join(reversed(words))
    return f"{last[:b]}{first[a:]}{mid}{first[:a]}{last[b:]}"


def brefix(phrase: str) -> str:
    """Returns each word with 'B' as prefix"""
    words = phrase.split()

    for i, word in enumerate(words):
        vi = vowel_index(word)
        words[i] = f"B{word[1:vi]}{word[vi:]}".title()

    return " ".join(words)


def tester(func: Callable, expectations: dict):
    for inp, outp in expectations.items():
        assert func(inp) == outp


def tests():
    tester(akshay_swap, {"Ceme Mode": "Meme Code", "yara da tashan": "tara da yashan"})
    tester(brefix, {"alia sharma": "Balia Bharma", "Moss Gaby": "Boss Baby"})
    print("All tests pass")


if __name__ == "__main__":
    print(akshay_swap("Ceme Mode"))
    print(brefix("Moss Gaby"))
    tests()
