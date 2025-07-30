import sqlite3

#connexion base de donnee
conn = sqlite3.connect("user.db", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL
)""")


cursor.execute("""CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    contenu TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
    )""")


cursor.execute("""DELETE FROM post""")
cursor.execute("""DELETE FROM user""")
conn.commit()


#verifier si la table est vide
cursor.execute("""SELECT COUNT(*) FROM user""")
user_count = cursor.fetchone()[0]

if user_count == 0 :
    cursor.execute("""INSERT INTO user (nom, prenom) VALUES("Diagne", "Lilou")""")
    cursor.execute("""INSERT INTO user (nom, prenom) VALUES("Legende", "LG")""")
    cursor.execute("""INSERT INTO user (nom, prenom) VALUES("Jamal", "Musiala")""")
    conn.commit()

print("liste des utilisateur")
cursor.execute("""SELECT * FROM user""")
for row in cursor.fetchall():
    print(row)
    
    
#recuperer id user
cursor.execute("""SELECT id FROM user""")
user_id = [row[0] for row in cursor.fetchall()]

print("liste des id user")
print(user_id)

cursor.execute("""SELECT COUNT(*) FROM post""")
post_count = cursor.fetchone()[0]


if post_count == 0 :
    cursor.execute("""INSERT INTO post (titre, contenu, user_id) VALUES("Post 1", "je suis un legende ", {})""".format(user_id[0]))
    cursor.execute("""INSERT INTO post (titre, contenu, user_id) VALUES("Post 2", "centre dinteret : Game", {})""".format(user_id[1]))
    cursor.execute("""INSERT INTO post (titre, contenu, user_id) VALUES("Post 3", "Joueur de foot professionnel", {})""".format(user_id[2]))
    conn.commit()



print("liste des post")
cursor.execute("""SELECT post.id, post.titre, post.contenu , user.nom, user.prenom FROM post JOIN user on post.user_id = user.id""")
for row in cursor.fetchall():
    print(row)
  
conn.close()
