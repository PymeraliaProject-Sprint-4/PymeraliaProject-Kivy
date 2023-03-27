import json  # importamos la libreria de python que nos permite trabajar con json
from pathlib import Path  # cargar ruta del script
import requests
import sqlite3
import threading
import time
conn = sqlite3.connect('pymeshield.db')

cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, recommendation TEXT NOT NULL, danger TEXT NOT NULL, manages TEXT NOT NULL, price FLOAT NULL, price_customer FLOAT NOT NULL)')
# cursor.execute('CREATE TABLE IF NOT EXISTS budgets (id INTEGER PRIMARY KEY, name TEXT NOT NULL, recommendation TEXT NOT NULL, danger TEXT NOT NULL, manages TEXT NOT NULL, price FLOAT NULL, price_customer FLOAT NOT NULL)')
conn.commit()
conn.close()
            
    