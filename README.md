# Mimoune 🌟

Une application web Flask pour gérer les commandes de produits cosmétiques et les réservations de sessions Hijama.

## 📋 Description

**Mimoune** est une plateforme e-commerce multilingue qui permet aux clients de :
- **Consulter et commander** des produits cosmétiques de qualité
- **Réserver des sessions** de Hijama (une thérapie traditionnelle)
- Contacter l'équipe via un formulaire de contact
- En savoir plus sur les services proposés

## ✨ Fonctionnalités

### 🧴 Gestion des Cosmétiques
- Affichage du catalogue de produits
- Système de commande avec formulaire
- Enregistrement des commandes en base de données
- Gestion des quantités commandées

### 💉 Réservation Hijama
- Formulaire de réservation avec date et heure
- Support du contenu en arabe et français
- Notes/commentaires personnalisés
- Validation côté serveur

### 📞 Services Supplémentaires
- Page de contact
- Page À propos
- Navigation intuitive
- Interface responsive

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner ou télécharger le projet**
   ```bash
   cd Mimoune
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv env
   ```

3. **Activer l'environnement virtuel**
   
   **Sur Windows :**
   ```bash
   env\Scripts\Activate.ps1
   ```
   
   **Sur macOS/Linux :**
   ```bash
   source env/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Utilisation

1. **Lancer l'application**
   ```bash
   python app.py
   ```

2. **Accéder à l'application**
   - Ouvrez votre navigateur
   - Allez à `http://localhost:5000`

3. **Navigation**
   - Page d'accueil : `/`
   - Cosmétiques : `/cosmetiques`
   - Hijama : `/hijama`
   - Contact : `/contact`
   - À propos : `/about`

## 📁 Structure du Projet

```
Mimoune/
├── app.py                 # Application principale Flask
├── requirements.txt       # Dépendances du projet
├── database.db           # Base de données SQLite (créée automatiquement)
├── templates/            # Fichiers HTML Jinja2
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── cosmetiques.html  # Page cosmétiques
│   ├── hijama.html       # Page Hijama
│   ├── contact.html      # Page contact
│   └── about.html        # Page À propos
├── static/               # Fichiers statiques
│   └── images/           # Images du site
└── env/                  # Environnement virtuel (local)
```

## 🛠️ Technologies Utilisées

| Technologie | Utilisation |
|------------|-------------|
| **Flask** | Framework web Python |
| **SQLite** | Base de données légère |
| **Jinja2** | Moteur de template (inclus dans Flask) |
| **HTML/CSS** | Interface utilisateur |
| **JavaScript** | Interactions côté client |

## 🗄️ Base de Données

L'application utilise **SQLite** avec deux tables principales :

### Table `commandes`
```sql
CREATE TABLE commandes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    telephone TEXT,
    produit TEXT,
    quantite INTEGER
);
```

### Table `reservations`
```sql
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    telephone TEXT,
    date TEXT,
    periode TEXT,
    notes TEXT
);
```

## 📝 Endpoints API

### GET
- `GET /` - Page d'accueil
- `GET /cosmetiques` - Catalogue cosmétiques
- `GET /hijama` - Page Hijama
- `GET /contact` - Page contact
- `GET /about` - Page À propos

### POST
- `POST /commander` - Soumettre une commande de produit
- `POST /reserver` - Soumettre une réservation Hijama

**Format des réponses :**
```json
{
    "statut": "succes|erreur",
    "message": "Message descriptif"
}
```

## ⚙️ Configuration

La base de données est initialisée automatiquement au premier lancement via la fonction `init_db()`.

Pour réinitialiser la base de données :
1. Supprimez le fichier `database.db`
2. Relancez l'application

## 📱 Support Multilingue

L'application supporte :
- 🇫🇷 Français
- 🇸🇦 Arabe

## 🔒 Sécurité

- Validation des formulaires côté serveur
- Requêtes SQL paramétrées (protection contre les injections SQL)
- Gestion basique des erreurs

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📄 License

Ce projet est fourni à titre de démonstration.

## 📧 Support

Pour toute question ou assistance, utilisez le formulaire de contact du site.

---

**Version** : 1.0.0  
**Dernière mise à jour** : 2026
