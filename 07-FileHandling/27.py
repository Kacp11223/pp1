import re
text = "To be, or not to be, that is the question"
def word(s):
    words = re.findall("\\b\w+\\b", s)
    return len(words)

print(word(text))