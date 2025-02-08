import psycopg2
import csv

# Database connection parameters
HOST = 'localhost'  # Or the container IP if running inside Docker
PORT = '5432'
DB_NAME = 'postgres'
USER = 'postgres'
PASSWORD = 'mysecretpassword'

# Path to the CSV file
CSV_FILE_PATH = 'users.csv'  # Make sure the path is correct

# Establishing connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD
    )
    cursor = connection.cursor()
    print("Connection to the database established successfully!")

    # Create a sample table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """)
    connection.commit()
    print("Table 'users' created or already exists.")

    # Open the CSV file and load data into the database
    with open(CSV_FILE_PATH, mode='r') as file:
        csv_reader = csv.DictReader(file)  # Read the CSV into a dictionary
        for row in csv_reader:
            # Prepare the insert statement
            insert_query = """
                INSERT INTO users (name, age)
                VALUES (%s, %s);
            """
            cursor.execute(insert_query, (row['name'], row['age']))
        connection.commit()

    print(f"Data from {CSV_FILE_PATH} inserted successfully into the 'users' table.")

    # Fetch and display data from the table
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    print("Data in the 'users' table:")
    for row in rows:
        print(row)

except Exception as error:
    print("Error while interacting with PostgreSQL:", error)
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Connection closed.")