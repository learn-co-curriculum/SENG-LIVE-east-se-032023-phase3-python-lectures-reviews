import sqlite3

CONN = sqlite3.connect('project_database.db')
CURSOR = CONN.cursor()