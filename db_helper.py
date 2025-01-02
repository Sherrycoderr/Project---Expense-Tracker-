import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'Localhost',      
    'user': 'root',   
    'password': '12345',  
    'database': 'expense_tracker',  
    'port': 3308
}

def initialize_db():
    """Initialize the MySQL database and create the table if it doesn't exist."""
    try:
        # Connect to the database
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                category VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure both cursor and connection are closed safely
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass
        if conn:
            conn.close()

def add_expense(name, price, category):
    """Add an expense to the MySQL database."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (name, price, category) VALUES (%s, %s, %s)", (name, price, category))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_expense(expense_id):
    """Delete an expense from the MySQL database by its ID."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def fetch_expenses():
    """Fetch all expenses from the MySQL database."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def calculate_total_expense():
    """Calculate the total expense from the MySQL database."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(price) FROM expenses")
        result = cursor.fetchone()
        return result[0] if result[0] else 0.0
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0.0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def reset_expenses():
    """Reset all expenses by clearing the MySQL database table."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE expenses")  # Clears all data but keeps table structure
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
