```python3
import re

def akshay_swap(phrase):
    words = phrase.split()
    n_words = len(words)
    if n_words == 2:
        first, last = words
        mid = ' '
    elif n_words == 3:
        first, mid, last = words
        mid = f" {mid} "
    else:
        return "You are MEME illiterate"
    vowels = r'[aeiouyAEIOUY@03]'
    try:
        a = re.search(vowels, first).span()[0]
        b = re.search(vowels, last).span()[0]
    except AttributeError as e:
        return " ".join(reversed(words))
    return f"{last[:b]}{first[a:]}{mid}{first[:a]}{last[b:]}"

print(akshay_swap("Ceme Mode"))
```

<img src="https://humornama.com/wp-content/uploads/2020/10/Akshay-Kumar-Swap-meme-template-of-Ajnabee-1122x1262.jpg" style=" width:500px ; height:600px "  >
