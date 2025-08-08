def compter_voyelle(word):
    _word = word.lower()    
    List_voyelle = ["a", "e", "i", "o", "u", "y"]
    compteur = 0
    for voyelle in _word:
        if voyelle in List_voyelle:
            compteur += 1
    return compteur

word = input("donner un mot :")
print(
    "le nombre de voyelle dans le mot " 
    + word + " est :" +str(compter_voyelle(word))
    
    + "\n"
    + " avec comme 1er lettre : " + word[0]
    + "\n"
    + " avec comme derniere lettre : " + word[-1]
    )

