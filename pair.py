number = input("donner un nombre :")
number = int(number)


if number == 0 :
    print("le nombre est null")
else:
    if number < 0 :
        print("le nombre est negatif")
    else:
        print("le nombre est positif")
    if number % 2 == 0 :
        print("le nombre est pair")
    else:
        print("le nombre est impair")
