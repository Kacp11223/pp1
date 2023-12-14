import json

movie = {
    "title" : "the good, the bad and the ugly",
    "year" : 1966,
    "actor" : {
        "leading" : "CLint Eastwood", 
        "supporting" : ["Eli Wallach","Lee Van Cleef"]},
    "oscar" : False
}

with open(r"C:\\Users\\melko\\Desktop\\pythonFilesHandling\\favorite.json","w") as f:
    json.dump(movie,f,indent=4)