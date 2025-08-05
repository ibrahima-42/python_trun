def verifier_mdp(mdp):
    caracteres_speciaux = "!@#$%^&*()-_"

    mdp_valide = (
        len(mdp) >= 8
        and any(c.islower() for c in mdp)
        and any(c.isupper() for c in mdp)
        and any(c.isdigit() for c in mdp)
        and any(c in caracteres_speciaux for c in mdp)
    )
    
    if mdp_valide :
        print("✅ le mot de passe est valide")
    else :
        print("❌ le mot de passe n'est pas valide")
        if len(mdp) < 8 :
            print("❌ le mot de passe doit contenir au moins 8 caracteres")
        if not any(c.islower() for c in mdp) :
            print("❌ le mot de passe doit contenir au moins un lettre minuscule")
        if not any(c.isupper() for c in mdp) :
            print("❌ le mot de passe doit contenir au moins un lettre majuscule")
        if not any(c.isdigit() for c in mdp) :
            print("❌ le mot de passe doit contenir au moins un chiffre")
        if not any(c in caracteres_speciaux for c in mdp) :
            print("❌ le mot de passe doit contenir au moins un caractere special")
            
mdp = input("donner un mot de passe : ")
verifier_mdp(mdp)