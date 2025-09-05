import sqlite3

conn = sqlite3.connect("data/authors.db")

cursor = conn.cursor()


def id_author_dict():
    id_author = {}
    cursor.execute("SELECT * from author;")
    rows = cursor.fetchall()
    for id, author in rows:
        id_author[id] = author
    return id_author
