import xml.etree.ElementTree as JM

#charger le ficher xml
affichage = JM.parse("etudiants.xml")
legende =  affichage.getroot()

for etudiant in legende.findall("etudiant"):
    id = etudiant.find("id").text
    nom = etudiant.find("nom").text
    prenom = etudiant.find("prenom").text
    age = etudiant.find("age").text
    filiere = etudiant.find("filiere").text
    

    print("ID:" +id)
    print("Nom:" +nom)
    print("Prenom:" +prenom)
    print("Age:" +age)
    print("Filiere:" +filiere)
    print("----------------")