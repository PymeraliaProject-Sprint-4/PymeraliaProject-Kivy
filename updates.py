import json
import requests
import sqlite3
from datetime import datetime
from kivy.storage.jsonstore import JsonStore
from sqlalchemy import Float, create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir conexión a la base de datos
engine = create_engine('sqlite:///pymeshield.db', echo=True)

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    price = Column(String)
    accepted = Column(String)

class Inventory(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    description = Column(String)
    state = Column(String)
    serial_number = Column(String)
    mac_ethernet = Column(String)
    mac_wifi = Column(String)

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recommendation = Column(String)
    danger = Column(String)
    manages = Column(String)
    price = Column(Float)
    price_customer = Column(Float)

def insert_data(data, table):
    session = Session()
    session.query(table).delete()
    for item in data:
        session.add(table(**item))
    session.commit()
    session.close()

def dataBudgets(data):
    insert_data(data, Budget)

def dataInventory(data):
    insert_data(data, Inventory)

def dataReports(data):
    insert_data(data, Report)

def dataCourses(data):
    insert_data(data, Course)

def dataTasks(data):
    insert_data(data, Task)

# api_data = []
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
