import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="librarydb"
)

cursor = db.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255)
)
""")

def add_book(title, author):
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    db.commit()
    print("Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)

# Example usage
add_book("The Alchemist", "Paulo Coelho")
add_book("Python Programming", "John Zelle")

print("\nLibrary Books:")
view_books()
