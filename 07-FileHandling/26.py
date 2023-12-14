import re
text = "To be, or not to be, that is the question"
def vowel(s):
    vowels = re.findall("[aiueo]", s)
    return len(vowels)

print(vowel(text))