from tokenize import endpats
from flask import Flask, jsonify, request, redirect
import xml.etree.ElementTree as ET

app = Flask(__name__)

etudiant_xml = ET.parse("etudiants.xml")
legende = etudiant_xml.getroot()

end_point = "/api/v1/etudiant"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": """Bienvenue sur mon 1er API avec flask crud etudiant xml contenant les informations des etudiants""",
        "end_point (liste des point entrer)": {
            "liste des etudiant": end_point + "/all-etudiant",
            "ajouter etudiant": end_point + "/add-etudiant",
            "supprimer etudiant": end_point + "/delete-etudiant/<id>"
        }
    })

@app.route(end_point + "/all-etudiant", methods=["GET"])
def get_etudiant():
    list_etudiant = []
    for etu in legende.findall("etudiant"):
        list_etudiant.append({
            "id": etu.find("id").text if etu.find("id") is not None else "",
            "nom": etu.find("nom").text ,
            "prenom": etu.find("prenom").text,
            "age": etu.find("age").text,
            "filiere": etu.find("filiere").text
        })
    return jsonify(list_etudiant)

@app.route(end_point + "/add-etudiant", methods=["POST"])
def post_etudiant():
    try:
        id = request.form["id"]
        name = request.form["nom"]
        prenom = request.form["prenom"]
        age = request.form["age"]
        filiere = request.form["filiere"]
    except KeyError:
        return jsonify({"message": "Paramètres manquants"}), 400
    new_etudiant = ET.Element("etudiant")
    ET.SubElement(new_etudiant, "id").text = id
    ET.SubElement(new_etudiant, "nom").text = name
    ET.SubElement(new_etudiant, "prenom").text = prenom
    ET.SubElement(new_etudiant, "age").text = age
    ET.SubElement(new_etudiant, "filiere").text = filiere
    legende.append(new_etudiant)
    etudiant_xml.write("etudiants.xml")
    # return jsonify({"message": "Étudiant ajouté avec succès"}), 201
    return redirect(end_point + "/all-etudiant")

@app.route(end_point + "/delete-etudiant/<id>", methods=["DELETE"])
def delete_etudiant(id):
    for etu in legende.findall("etudiant"):
        if etu.find("id").text == id:
            legende.remove(etu)
            etudiant_xml.write("etudiants.xml")
            return jsonify({"message" : "Etudiant supprimé avec succès"}), 200
    return jsonify({"message" : "Etudiant non trouve"}), 404

@app.route(end_point + "/update-etudiant", methods=["POST"])
def update_etudiant():
    try:
        id = request.form["id"]
        name = request.form["nom"]
        prenom = request.form["prenom"]
        age = request.form["age"]
        filiere = request.form["filiere"]
    except KeyError:
        return jsonify({"message": "Parametre maquante"}), 400
    for etu in legende.findall("etudiant"):
        if etu.find("id").text == id:
            etu.find("nom").text = name
            etu.find("prenom").text = prenom
            etu.find("age").text = age
            etu.find("filiere").text = filiere
            etudiant_xml.write("etudiants.xml")
        return redirect(end_point + "/all-etudiant")
    return jsonify({"message" : "Etudiant non trouve"}), 404

if __name__ == "__main__":
    app.run(debug=True)
