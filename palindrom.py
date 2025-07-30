
def is_palindrom(word):
    _word = word.lower()
    return _word == _word[::-1]

word = input("donner un mot :")
if is_palindrom(word):
    print("le mot est un palindrom")
else:
    print("le mot n'est pas un palindrom")