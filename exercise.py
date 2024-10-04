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

print("\n\033[1;32mTables créées avec succès.\033[0m\n")

# Récupération de la liste de tous les clients
cursor.execute('SELECT * FROM Clients')
clients = cursor.fetchall()

# Affichage des clients
print("\033[1;36mListe des clients :\033[0m")
for client in clients:
    print(f"ID: {client[0]}, Nom: {client[1]}, Prénom: {client[2]}, Email: {client[3]}, Date d'inscription: {client[4]}")
print()

# Récupérer les informations du client (nom, prénom) en utilisant l'id
client_id = 5
cursor.execute('''
    SELECT nom, prenom FROM Clients WHERE id = ?
''', (client_id,))

client = cursor.fetchone()

if client:
    nom, prenom = client
    print(f"Liste des commandes de \033[1;36m{nom} {prenom}\033[0m:")

    # Récupérer les commandes du client en utilisant son client_id
    cursor.execute('''
        SELECT produit, date_commande FROM Commandes WHERE client_id = ?
    ''', (client_id,))
    
    commandes = cursor.fetchall()

    # Afficher les commandes du client
    if commandes:
        for idx, commande in enumerate(commandes, 1):
            produit, date_commande = commande
            print(f"- Commande {idx}: {produit}, passée le {date_commande}")
        print()
    else:
        print("\033[91mAucune commande trouvée pour ce client.\033[0m\n")
else:
    print("\033[91mClient non trouvé.\033[0m\n")

# Mettre à jour l'adresse email du client avec l'id 5
nouvel_email = 'emma.garcia@gmail.com'
client_id = 5

cursor.execute('''
    UPDATE Clients
    SET email = ?
    WHERE id = ?
''', (nouvel_email, client_id))

# Sauvegarder les changements
connection.commit()

# Vérifier si la mise à jour a bien été effectuée
cursor.execute('SELECT nom, prenom, email FROM Clients WHERE id = ?', (client_id,))
client = cursor.fetchone()
print(f"Client \033[1;36m{client[1]} {client[0]}\033[0m a maintenant l'email : \033[1;36m{client[2]}\033[0m\n")

# Suppression de la commande avec l'id 4
commande_id = 4
cursor.execute('''
    DELETE FROM Commandes
    WHERE id = ?
''', (commande_id,))

# Sauvegarder les changements
connection.commit()

print(f"Commande numéro \033[1;36m{commande_id}\033[0m supprimée\n")

# Fermer la connexion
connection.close()
