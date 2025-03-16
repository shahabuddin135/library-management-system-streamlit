import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from util import db_connect

# Load environment variables (for local development)
db_connect()
load_dotenv()


def get_connection():
    """
    Connect to Neon using credentials from Streamlit secrets or .env.
    """
    conn_str = st.secrets["neon"]["url"] if "neon" in st.secrets else os.getenv("NEON_DATABASE_URL")
    try:
        return psycopg2.connect(conn_str)
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

def create_table():
    """Create the books table if it does not exist."""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL,
                    year INTEGER,
                    read_status BOOLEAN DEFAULT FALSE,
                    available BOOLEAN DEFAULT TRUE,
                    genre VARCHAR(100)
                );
            """)
            conn.commit()
        finally:
            cur.close()
            conn.close()

def add_book(title, author, year, available, read_status, genre):
    """Insert a new book record."""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO books (title, author, year, available, read_status, genre) VALUES (%s, %s, %s, %s, %s, %s)",
                (title, author, year, available, read_status, genre)
            )
            conn.commit()
        finally:
            cur.close()
            conn.close()

def get_books():
    """Retrieve all book records."""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books ORDER BY id")
            rows = cur.fetchall()
            return rows
        finally:
            cur.close()
            conn.close()
    return []

def update_book(book_id, title, author, year, read_status, available, genre):
    """Update an existing book record."""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE books 
                SET title=%s, author=%s, year=%s, read_status=%s, available=%s, genre=%s 
                WHERE id=%s
                """,
                (title, author, year, read_status, available, genre, book_id)
            )
            conn.commit()
        finally:
            cur.close()
            conn.close()

def delete_book(book_id):
    """Delete a book record."""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
            conn.commit()
        finally:
            cur.close()
            conn.close()

# Create the table on startup
create_table()

st.title("Library Management System")

menu = ["Add Book", "View Books", "Update Book", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.header("Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year", min_value=1000, max_value=2100, step=1)
        read_status = st.checkbox("Read?", value=False)
        available = st.checkbox("Available", value=True)
        genre = st.text_input("Genre")
        submitted = st.form_submit_button("Add Book")
        if submitted and title and author:
            add_book(title, author, year, available, read_status, genre)
            st.success(f"Book '{title}' added successfully!")
        elif submitted:
            st.error("Title and Author are required.")

elif choice == "View Books":
    st.header("View Books")
    books = get_books()
    if books:
        df = pd.DataFrame(books, columns=["ID", "Title", "Author", "Year", "Read Status", "Available", "Genre"])
        st.dataframe(df)
    else:
        st.info("No books found in the database.")

# Ensure session state key is initialized
if "book_data" not in st.session_state:
    st.session_state.book_data = None

elif choice == "Update Book":
    st.header("Update Book")
    book_id = st.number_input("Enter Book ID to update", min_value=1, step=1)
    
    if st.button("Fetch Book"):
        books = get_books()
        book = next((b for b in books if b[0] == book_id), None)
        if book:
            st.session_state.book_data = book
        else:
            st.session_state.book_data = None
            st.error("Book not found.")

    if st.session_state.book_data:
        book = st.session_state.book_data
        with st.form("update_book_form"):
            title = st.text_input("Title", value=book[1])
            author = st.text_input("Author", value=book[2])
            year = st.number_input("Year", min_value=1000, max_value=2100, step=1, value=book[3] or 2000)
            read_status = st.checkbox("Read?", value=book[4] if book[4] is not None else False)
            available = st.checkbox("Available", value=book[5] if book[5] is not None else True)
            genre = st.text_input("Genre", value=book[6] if book[6] else "")
            submitted = st.form_submit_button("Update Book")
            if submitted:
                update_book(book_id, title, author, year, read_status, available, genre)
                st.success(f"Book ID {book_id} updated successfully!")

elif choice == "Delete Book":
    st.header("Delete Book")
    book_id = st.number_input("Enter Book ID to delete", min_value=1, step=1)
    if st.button("Delete Book"):
        delete_book(book_id)
        st.success(f"Book ID {book_id} deleted successfully!")
