import random

def deviner_nombre():
    nombre_secret = random.randint(1, 20)
    essai = None
    tentatives = 0
    
    print("Deviner le nombre choisi par l'ordinateur entre 1 et 20")
    
    while True:
        try :
            essai = int(input("donner un nombre :"))
            tentatives += 1
            if essai < nombre_secret:
                print("nombre trop petit")
            elif essai > nombre_secret:
                print("nombre trop grand")
            else:
               print("🎉 Bravo ! Tu as trouvé le bon nombre !")
               print("👉 Nombre de tentatives : " + str(tentatives))
               print("🔐 Le nombre secret était : " + str(nombre_secret))
               print("Merci d'avoir joué ! 😊")
               break
        except ValueError:
            print("veuillez entrer un nombre valide")
            
def main():
    deviner_nombre()

if __name__ == "__main__":
    main()