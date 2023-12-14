ICAO = {
    "a":"alpha",
    "b":"bravo",
    "c":"charlie",
    "d":"delta",
    "e":"echo",
    "f":"foxtrot",
    "g":"golf",
    "h":"hotel",
    "i":"india",
    "j":"juliet",
    "k":"kilo",
    "l":"lima",
    "m":"mike",
    "n":"november",
    "o":"oscar",
    "p":"papa",
    "q":"quebec",
    "r":"romeo",
    "s":"sierra",
    "t":"tango",
    "u":"uniform",
    "v":"victor",
    "w":"whiskey",
    "x":"x-ray",
    "y":"yankee",
    "z":"zulu"
}

word = input("type something ")

def ICAOtrans(s):
    return " ".join([ICAO[x] for x in s])

print(ICAOtrans(word))