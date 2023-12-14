def numWords(s):
    return len(s.split(' '))

string = "An apple a day keeps the doctor away"

print(numWords(string))

def wordSort(s):
    aux = s.split(' ')
    return [y[1] for y in sorted([(len(x),x) for x in aux])]

print(wordSort(string))

def alphabetical(s):
    return sorted(wordSort(s))

print(alphabetical(string))