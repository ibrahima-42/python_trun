from flask import Flask, request, redirect, render_template
import sqlite3
app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register() :
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    if request.method == "POST" :
        try :
            nom = request.form["nom"]
            prenom = request.form["prenom"]
            email = request.form["email"]
            password = request.form["password"]
            cursor.execute("""INSERT INTO user (nom, prenom, email, password) VALUES (?, ?, ?, ?)""", (nom, prenom, email, password))
            conn.commit()
            print("user ajouter avec succes")
        except Exception as e :
            print("error : " +str(e))
        return redirect("/login")   
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login() :
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    if request.method == "POST" :
        try :
            email = request.form["email"]
            password = request.form["password"]
            cursor.execute("""SELECT * FROM user WHERE email = ? AND password = ?""", (email, password))
            user = cursor.fetchone()
            conn.commit()
            if user :
                print("user connecté avec succes")
            else :
                print("user non trouve")
        except Exception as e :
            print("error : " +str(e))
        return redirect("/liste")   
    return render_template("login.html")
    
def main() :
    register()
    login()

if __name__ == "__main__" :
    app.run(debug=True)
    main()
