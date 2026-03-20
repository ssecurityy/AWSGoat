import sqlite3
import os

def get_user(username):
    """VULNERABLE: SQL injection via string concatenation."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def search_products(keyword):
    """VULNERABLE: Another SQL injection."""
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{keyword}%'")
    return cursor.fetchall()
