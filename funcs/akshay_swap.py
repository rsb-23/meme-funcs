import re


def akshay_swap(phrase):
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
    vowels = r"[aeiouyAEIOU@03]"
    try:
        a = re.search(vowels, first.title()).span()[0]
        b = re.search(vowels, last.title()).span()[0]
    except AttributeError:
        return " ".join(reversed(words))
    return f"{last[:b]}{first[a:]}{mid}{first[:a]}{last[b:]}"


if __name__ == "__main__":
    print(akshay_swap("Ceme Mode"))
