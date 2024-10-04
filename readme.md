# SQLite Database Management with Python

<img src="https://github.com/TonyVallad/Introduction-SQLite/blob/main/sqlite-introduction.png?raw=true" width="850"/>

This project demonstrates how to create, manipulate, and export data from an SQLite database using Python. It includes the creation of two tables (`Clients` and `Commandes`), inserting fictional data, updating and deleting records, and exporting the data to CSV files.

## Project Structure

- **database.db**: SQLite database file created and manipulated by the Python scripts.
- **clients.csv**: Exported CSV file containing data from the `Clients` table.
- **commandes.csv**: Exported CSV file containing data from the `Commandes` table.
- **exercise.py**: Python script that manages the SQLite database (creation, insertion, querying, updating, and deletion).
- **export-to-csv.py**: Python script to export the contents of the `Clients` and `Commandes` tables into CSV files.

## Features

1. **Database Creation**:
   - Creates a `Clients` table to store client information (ID, name, email, date of registration).
   - Creates a `Commandes` table to store order information (ID, client ID as foreign key, product, and order date).

2. **Data Insertion**:
   - Inserts 5 fictional clients and 8 orders into the database.

3. **Querying**:
   - Retrieves and displays all clients.
   - Fetches orders for a specific client by ID (e.g., Emma Garcia).

4. **Updating**:
   - Updates the email of a client based on their ID.

5. **Deletion**:
   - Deletes a specific order from the database by order ID.

6. **Data Export**:
   - Exports the contents of the `Clients` and `Commandes` tables to two separate CSV files using `export-to-csv.py`.

## Prerequisites

- Python 3.x
- SQLite3 (downloaded from [SQLite official site](https://www.sqlite.org/download.html))
- `csv` library (comes pre-installed with Python)

## Usage

### Running the Main Script (`exercise.py`):

1. Clone the repository or copy the script.
2. Ensure Python and SQLite3 are installed on your system.
3. Run the script using the command:

    ```bash
    python exercise.py
    ```

4. The script will:
   - Create the database and tables (if they don’t already exist).
   - Insert data into the tables.
   - Display the list of clients and their orders.
   - Update the email of a client.
   - Delete an order.

### Exporting Data to CSV (`export-to-csv.py`):

1. Run the script using the command:

    ```bash
    python export-to-csv.py
    ```

2. The script will:
   - Export the contents of the `Clients` table to `clients.csv`.
   - Export the contents of the `Commandes` table to `commandes.csv`.

## Example Output

After running the main script, you should see output like:

```
Tables créées avec succès.

Liste des clients :
ID: 1, Nom: Roche, Prénom: Alice, Email: alice.roche@example.com, Date d'inscription: 2024-01-15
...

Liste des commandes de Garcia Emma:
- Commande 1: Vélo Électrique GreenRide, passée le 2024-09-01
- Commande 2: Casque VR UltraVision, passée le 2024-09-18

Client Emma Garcia a maintenant l'email : emma.garcia@gmail.com

Commande numéro 4 supprimée
```

## Files Generated

- **clients.csv**: Contains all client data.
- **commandes.csv**: Contains all order data.

## License

This project is open-source and available for modification and distribution. Please feel free to use it for educational purposes.