from flask import Flask , render_template
import sqlite3

app = Flask(__name__)

@app.route("/liste")
def home():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM user""")
    users = cursor.fetchall()
    
    cursor.execute("""SELECT post.id, post.titre, post.contenu , user.nom
                   , user.prenom FROM post JOIN user ON post.user_id = user.id""")
    posts = cursor.fetchall()
    
    conn.close()
    
    return render_template("index.html", users=users, posts=posts)

if __name__ == "__main__":
    app.run(debug=True)