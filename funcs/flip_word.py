from funcs.tester import tester


def rotate_180(word: str) -> str:
    """
    Rotates word by 180 degrees and returns the rotated phrase.

    This function reverses the input string and maps each character to its
    corresponding ASCII character after a 180-degree rotation. Only specific
    characters are mapped, while others remain unchanged.

    Letters that don't change on rotation : 'losxz-HINOSXZ 058'
    """

    # fmt: off
    rotate_map_180 = {
        'a': 'e', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'a',
        'f': 'ɟ', 'g': 'ƃ', 'h': 'y', 'i': 'ᴉ', 'j': 'ɾ',
        'k': 'ʞ', 'l': 'l', 'm': 'w', 'n': 'u', 'o': 'o',
        'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ',
        'u': 'n', 'v': 'ʌ', 'w': 'm', 'x': 'x', 'y': 'h', 'z': 'z',
        'A': '∀', 'B': 'q', 'C': 'Ↄ', 'D': 'p', 'E': 'Ǝ',
        'F': 'Ⅎ', 'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ſ',
        'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O',
        'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': 'S', 'T': '⊥',
        'U': '∩', 'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        '0': '0', '1': '⇂', '2': '↊', '3': '↋', '4': 'ᔭ',
        '5': '5', '6': '9', '7': 'Ɫ', '8': '8', '9': '6',
        '.': '˙', ',': "'", '?': '¿', '!': '¡', '"': '„', "'": ',', '`': '‘',
        '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<'
    }
    # fmt: on
    return "".join(rotate_map_180.get(char, char) for char in reversed(word))


def tests():
    tester(rotate_180, {"hoq uewom": "woman boy", "woman boy": "hoq uewom"})
    tester(rotate_180, {"losxz-HINOSXZ 058": "850 ZXSONIH-zxsol"})  # unchanged chars
    print("All tests pass")


if __name__ == "__main__":
    tests()
