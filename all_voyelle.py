def all_voyelle(word):
    word_set = set(word.lower()) # convertir le mot en ensembles de voyelle
    voyelles = set("aeiouy") # convertir les voyelles en ensembles
    return voyelles.issubset(word_set) # verifier si le mot contient tout les voyelles
        
word = input("donner un mot : ")
if all_voyelle(word):
    print("le mot " + word + " contient tout les voyelle")
else:
    print("le mot " + word + " n'est pas contient tout les voyelle")