import sqlite3

# Connexion à la base de données (création si elle n'existe pas)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Création de la table Clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    date_inscription DATE NOT NULL
)
''')

# Création de la table Commandes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Commandes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    produit TEXT NOT NULL,
    date_commande DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients (id) ON DELETE CASCADE
)
''')

# Insertion de 5 clients fictifs
clients = [
    ('Roche', 'Alice', 'alice.roche@example.com', '2024-01-15'),
    ('Blanc', 'Olivier', 'olivier.blanc@example.com', '2024-02-10'),
    ('Carpentier', 'Marie', 'marie.carpentier@example.com', '2024-03-05'),
    ('Fontaine', 'Lucas', 'lucas.fontaine@example.com', '2024-04-20'),
    ('Garcia', 'Emma', 'emma.garcia@example.com', '2024-05-12')
]

cursor.executemany('''
INSERT INTO Clients (nom, prenom, email, date_inscription)
VALUES (?, ?, ?, ?)
''', clients)

# Insertion de 4 commandes fictives, avec les client_id correspondants
commandes = [
    (1, 'Robot Aspirateur X500', '2024-06-01'),
    (1, 'Cafetière Expresso', '2024-06-10'),
    (2, 'Télévision OLED 55"', '2024-07-02'),
    (2, 'Barre de son HomeCinema', '2024-07-10'),
    (3, 'Chaise Ergonomique ConfortPlus', '2024-07-25'),
    (4, 'Smartphone Quantum 12', '2024-08-12'),
    (5, 'Vélo Électrique GreenRide', '2024-09-01'),
    (5, 'Casque VR UltraVision', '2024-09-18')
]

cursor.executemany('''
INSERT INTO Commandes (client_id, produit, date_commande)
VALUES (?, ?, ?)
''', commandes)

# Sauvegarder les changements
connection.commit()

# Fermer la connexion
connection.close()

print("\n\033[1;32mTables créées avec succès.\033[0m\n")
