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
api_data2 = []
api = "http://localhost/api/"

def get_api(url):

    url = api + url
    response = requests.get(url)
    data = json.loads(response.text)
    api_data = data['data']
    # self.insert_data();
    return api_data

def get_api_data(url):
    
    url = api + url
    response = requests.get(url)
    data = json.loads(response.text)
    api_data2 = data
    # self.insert_data();
    return api_data2

def Update():
    #Recuperar company_id session y transformar en string para poder hacer la petición a la Api
    session = JsonStore('session.json')
    session_user_type = session.get('type')['type']
    session_companyID = None

    if(session_user_type == 'client'):
        session_companyID = str(session.get('company_id')['company_id'])
        datainventories = get_api_data('devicelist/' + session_companyID)
    else:
        datainventories = get_api_data('devicelist/')

    


    datacourses = get_api_data('couser-user-data')
    datatasks = get_api('all-data')
    databudgets = get_api_data('budgets-data')
    datareports = get_api_data('kivy/report')
    dataTasks(datatasks)
    dataBudgets(databudgets)
    dataReports(datareports)
    dataCourses(datacourses)
    dataInventory(datainventories)
