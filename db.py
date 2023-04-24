import sqlite3

def CreateDB():
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, recommendation TEXT NOT NULL, danger TEXT NOT NULL, manages TEXT NOT NULL, price FLOAT NULL, price_customer FLOAT NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS budgets (id INTEGER PRIMARY KEY, price FLOAT NULL, accepted TEXT NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, name TEXT NOT NULL, status TEXT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS inventories (id INTEGER PRIMARY KEY, brand TEXT NULL, model TEXT NULL, state TEXT NULL, serial_number TEXT NULL, mac_ethernet TEXT NULL, mac_wifi TEXT NULL, description TEXT NULL)')

    conn.commit()
    conn.close()
            
    