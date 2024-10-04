# SQLite Database Management with Python

<img src="https://github.com/TonyVallad/Introduction-SQLite/blob/main/sqlite-introduction.png?raw=true" width="750"/>

This project demonstrates how to create, manipulate, and export data from an SQLite database using Python. It includes the creation of two tables (`Clients` and `Commandes`), inserting fictional data, updating and deleting records, and exporting the data to CSV files.

## Project Structure

- **database.db**: SQLite database file created and manipulated by the Python script.
- **clients.csv**: Exported CSV file containing data from the `Clients` table.
- **commandes.csv**: Exported CSV file containing data from the `Commandes` table.
- **script.py**: Main Python script that manages the SQLite database.

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
   - Exports the contents of the `Clients` and `Commandes` tables to two separate CSV files.

## Prerequisites

- Python 3.x
- SQLite3 (comes pre-installed with Python)
- `csv` library (comes pre-installed with Python)

## Usage

1. Clone the repository or copy the script.
2. Ensure Python is installed on your system.
3. Run the script using the command:

    ```bash
    python script.py
    ```

4. The script will:
   - Create the database and tables (if they don’t already exist).
   - Insert data into the tables.
   - Display the list of clients and their orders.
   - Update the email of a client.
   - Delete an order.
   - Export the data to `clients.csv` and `commandes.csv`.

## Example Output

After running the script, you should see output like:

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

This project is open-source and available under the MIT License.
```

### How to use it:
- **Project Title**: Provides an overview of what the project does.
- **Features**: Lists the functionalities of the script.
- **Prerequisites**: Explains the tools required to run the project.
- **Usage**: Step-by-step instructions on how to run the script.
- **Example Output**: Shows an example of what the user will see in the terminal when they run the script.
- **Files Generated**: Indicates which files will be created when the script is executed.