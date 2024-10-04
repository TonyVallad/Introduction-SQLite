import csv
import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Exporter la table Clients dans un fichier CSV
cursor.execute('SELECT * FROM Clients')
clients = cursor.fetchall()

with open('clients.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Écrire l'en-tête des colonnes
    csvwriter.writerow(['id', 'nom', 'prenom', 'email', 'date_inscription'])
    # Écrire les données des clients
    csvwriter.writerows(clients)

print("Table Clients exportée avec succès dans 'clients.csv'.")

# Exporter la table Commandes dans un fichier CSV
cursor.execute('SELECT * FROM Commandes')
commandes = cursor.fetchall()

with open('commandes.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Écrire l'en-tête des colonnes
    csvwriter.writerow(['id', 'client_id', 'produit', 'date_commande'])
    # Écrire les données des commandes
    csvwriter.writerows(commandes)

print("Table Commandes exportée avec succès dans 'commandes.csv'.")

# Fermer la connexion
connection.close()
