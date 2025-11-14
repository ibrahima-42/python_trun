from flask import Flask , render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/liste")
def liste():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM user""")
    users = cursor.fetchall()
    
    cursor.execute("""SELECT post.id, post.titre, post.contenu , user.nom
                   , user.prenom FROM post JOIN user ON post.user_id = user.id""")
    posts = cursor.fetchall()
    
    conn.close()
    
    return render_template("index.html", users=users, posts=posts)

#detail user function
@app.route("/detail/user/<id>")
def detail_user(id):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user WHERE id = ?",(id,))
    user = cursor.fetchone()
    conn.close()
    
    if user :
        return render_template("detail.html", user=user)
    else :
        return jsonify({"message": "Utilisateur non trouve"}), 404

#ajout user function
@app.route("/add/user", methods=["GET","POST"])
def add_user():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    
    if request.method == "POST" :
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        
        cursor.execute("INSERT INTO user (nom, prenom) VALUES(?, ?)",(nom, prenom))
        conn.commit()
        conn.close()
        return redirect("/liste")
    
    return render_template("add.html")

#update user function
@app.route("/update/user/<id>", methods=["GET", "POST"])
def update_user(id):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    if request.method == "POST" :
       nom = request.form["nom"]
       prenom = request.form["prenom"]
       cursor.execute("UPDATE user SET nom = ? , prenom = ? WHERE id = ?",(nom,prenom,id))
       conn.commit()
       conn.close()
       return redirect("/liste")
    
    cursor.execute("SELECT * FROM user WHERE id = ?",(id,))
    user = cursor.fetchone()
    conn.close()
    
    if user :
        return render_template("update.html", user=user)
    else :
        return jsonify({"message": "Utilisateur non trouve"}), 404
    
    
#delete user fuction
@app.route("/delete/user/<id>", methods=["GET", "POST"])
def delete_user(id):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM user WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect("/liste")


#add post function
@app.route("/add/post", methods=["GET", "POST"])
def add_post():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    if request.method == "POST" :
        titre = request.form["titre"]
        contenu = request.form["contenu"]
        user_id = request.form["user_id"]
        
        cursor.execute("INSERT INTO post (titre, contenu, user_id) VALUES(?, ?, ?)", (titre, contenu, user_id))
        conn.commit()
        conn.close()
        return redirect("/liste")
    
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    conn.close()
    return render_template("add_post.html", users=users)

#update post function
@app.route("/update/post/<id>", methods=["GET", "POST"])
def update_post(id) :
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    if request.method == "POST" :
        titre = request.form["titre"]
        contenu = request.form["contenu"]
        user_id = request.form["user_id"]
        
        cursor.execute("UPDATE post SET titre = ? , contenu = ? , user_id = ? WHERE id = ?", (titre, contenu , user_id , id))
        conn.commit()
        conn.close()
        return redirect("/liste")
    
    cursor.execute("SELECT * FROM post WHERE id = ?", (id,))
    post = cursor.fetchone()
    
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    conn.close()
    
    if post :
        return render_template("update_post.html", post=post, users=users)
    else :
        return jsonify({"message" : "Post non trouver"}), 404

#delete post function
@app.route("/delete/post/<id>", methods=["GET", "POST"])
def delete_post(id) :
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM post WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/liste")

#function register
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

#login function
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
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6874, debug=True)