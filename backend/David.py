import sqlite3
import QueryCreator

def create_query(message):
    return QueryCreator.create_query(message)

def get_pdfs(query):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return [row[0] for row in rows if row[0] != '']