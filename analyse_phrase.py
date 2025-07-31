def analyse_phrase(phrase):
    phrase = phrase.lower()
    mots = phrase.split() #decouper la phrase en mots 
    nombre_de_mots = len(mots) #compter le nombre de mot
    nombre_de_caractere = len(phrase.replace(" ", "")) #compter le nombre de caractere sans espace 
    mot_le_plus_long = max(mots, key=len) #trouver le nombre le plus long 
    mot_le_plus_frequent = max(mots, key=mots.count) #trouver le mot le plus frequent 
    
    return {
        "nombre_de_mots": nombre_de_mots,
        "nombre_de_caractere": nombre_de_caractere,
        "mot_le_plus_long": mot_le_plus_long,
        "mot_le_plus_frequent": mot_le_plus_frequent
    }

mon_text = input("donner un texte : ")
print(analyse_phrase(mon_text))