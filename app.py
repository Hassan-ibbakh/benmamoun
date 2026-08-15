from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Fonction pour créer la base de données légère (SQLite)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Table des commandes de produits cosmétiques
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            telephone TEXT,
            produit TEXT,
            quantite INTEGER
        )
    ''')

    # Table des réservations Hijama
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            telephone TEXT,
            date TEXT,
            periode TEXT,
            notes TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Route pour la page d'accueil
@app.route('/')
def accueil():
    return render_template('index.html')

# Route pour traiter le formulaire de commande de produits
@app.route('/commander', methods=['POST'])
def commander():
    nom = request.form.get('nom')
    telephone = request.form.get('telephone')
    produit = request.form.get('produit')
    quantite = request.form.get('quantite')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO commandes (nom, telephone, produit, quantite) VALUES (?, ?, ?, ?)',
                   (nom, telephone, produit, quantite))
    conn.commit()
    conn.close()

    return jsonify({'statut': 'succes', 'message': 'Commande enregistrée !'})

# Route pour traiter le formulaire de réservation Hijama
@app.route('/reserver', methods=['POST'])
def reserver():
    nom = request.form.get('nom')
    telephone = request.form.get('telephone')
    date = request.form.get('date')
    periode = request.form.get('periode')
    notes = request.form.get('notes')

    # Validation minimale côté serveur
    if not nom or not telephone or not date or not periode:
        return jsonify({'statut': 'erreur', 'message': 'معلومات ناقصة'}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reservations (nom, telephone, date, periode, notes) VALUES (?, ?, ?, ?, ?)',
                   (nom, telephone, date, periode, notes))
    conn.commit()
    conn.close()

    return jsonify({'statut': 'succes', 'message': 'Réservation enregistrée !'})

# Route pour la page des cosmétiques
@app.route('/cosmetiques')
def cosmetiques():
    return render_template('cosmetiques.html')

# Route pour la page Hijama
@app.route('/hijama')
def hijama():
    return render_template('hijama.html')

# Route pour la page Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route pour la page A propos
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    init_db()  # Initialise la BDD au démarrage
    app.run(debug=True)  # Démarre le serveur