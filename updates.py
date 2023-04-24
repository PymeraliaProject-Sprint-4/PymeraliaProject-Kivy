import json  # importamos la libreria de python que nos permite trabajar con json
import requests
import sqlite3
from kivy.storage.jsonstore import JsonStore # libreria para las sesiones

def dataBudgets(data):
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM budgets')
    
    for i in data:
        id = int(i['id'])
        price = i['price']
        accepted = i['accepted']
        
        datos = [(id, price, accepted)]
        
        for dato in datos:
            cursor.execute('INSERT INTO budgets (id, price, accepted) VALUES (?, ?, ?)', dato)
            
            conn.commit()
        
    conn.close()
   
def dataInventory(data):
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM inventories')
    
    for i in data:
        id = int(i['id'])
        brand = i['brand']
        model = i['model']
        description = i['description']
        state = i['state']
        serial_number = i['serial_number']
        mac_ethernet = i['mac_ethernet']
        mac_wifi = i['mac_wifi']
        
        datos = [(id, brand, model, description, state, serial_number, mac_ethernet, mac_wifi)]
        
        for dato in datos:
            cursor.execute('INSERT INTO inventories (id, brand, model, description, state, serial_number, mac_ethernet, mac_wifi) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', dato)
            
            conn.commit()
        
    conn.close()
    
def dataReports(data):
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM reports')
    
    for i in data:
        id = int(i['id'])
        name = i['name']
        status = i['status']
        date = i['date']
        
        datos = [(id, name, status, date)]
        
        for dato in datos:
            cursor.execute('INSERT INTO reports (id, name, status, date) VALUES (?, ?, ?, ?)', dato)
            
            conn.commit()
        
    conn.close()
    
def dataCourses(data):
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM courses')
    
    for i in data:
        id = int(i['id'])
        name = i['name']
        description = i['description']
        date = i['date']
        
        datos = [(id, name, description, date)]
        
        for dato in datos:
            cursor.execute('INSERT INTO courses (id, name, description, date) VALUES (?, ?, ?, ?)', dato)
            
            conn.commit()
        
    conn.close()

def dataTasks(data):
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks')

    for i in data:
            id = int(i['id'])
            name = i['name']
            recommendation = i['recommendation']
            danger = i['peligro']
            manages = i['manages']
            price = i['price']
            price_customer = i['price_customer']

            datos = [(id, name, recommendation, danger,
                      manages, price, price_customer)]

            for dato in datos:
                cursor.execute(
                    'INSERT INTO tasks (id, name, recommendation, danger, manages, price, price_customer) VALUES (?, ?, ?, ?, ?, ?, ?)', dato)

                conn.commit()

    conn.close()

api_data = []
api = "http://localhost/api/"


def get_api_data(url):
    
    #Recuperar token session
    session = JsonStore('session.json')
    session_token = session.get('token')['token']

    # Configurar la cabecera de la solicitud GET
    headers = {'Authorization': 'Bearer ' + session_token}

    # Realizar la solicitud GET a la API
    # response = requests.get('http://localhost/api/user', headers=headers)
    
    url = api + url
    response = requests.get(url, headers=headers)
    print(response.text)
    data = json.loads(response.text)
    api_data = data
    # self.insert_data();
    return api_data

def Update():
    #Recuperar company_id session y transformar en string para poder hacer la petición a la Api
    datatasks = get_api_data('all-data-kivy')
    datainventories = get_api_data('devicelist/')
    datacourses = get_api_data('course-user-data')  
    databudgets = get_api_data('budgets-data')
    datareports = get_api_data('kivy/report')
    dataTasks(datatasks)
    dataBudgets(databudgets)
    dataReports(datareports)
    dataCourses(datacourses)
    dataInventory(datainventories)
