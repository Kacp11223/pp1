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

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\ICAO.json","w") as f:
    for key,values in ICAO.items():
        f.write('%s %s\n' % (key, values))