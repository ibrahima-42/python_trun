def pangramme(phrase) :
    phrase = phrase.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    phrase_set = set(phrase)
    return alphabet.issubset(phrase_set) #

phrase = input("donner une phrase :")

if pangramme(phrase) :
    print("la phrase (" + phrase + ") est un pangramme")
else :
    print("la phrase (" + phrase + ") n'est pas un pangramme")