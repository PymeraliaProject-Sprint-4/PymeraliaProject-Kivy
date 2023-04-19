import json  # importamos la libreria de python que nos permite trabajar con json
import requests
import sqlite3

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
api = "http://192.168.224.241/api/"

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
    datatasks = get_api('all-data')
    databudgets = get_api_data('budgets-data')
    datareports = get_api_data('kivy/report')
    datacourses = get_api_data('couser-user-data')
    dataTasks(datatasks)
    dataBudgets(databudgets)
    dataReports(datareports)
    dataCourses(datacourses)
