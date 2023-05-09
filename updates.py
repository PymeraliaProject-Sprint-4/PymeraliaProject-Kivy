import json
from utils import ControlApi, Notify
from sqlalchemy import Float, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir conexión a la base de datos
engine = create_engine("sqlite:///pymeshield.db")

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    price = Column(String)
    accepted = Column(String)


class Inventory(Base):
    __tablename__ = "inventories"
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    description = Column(String)
    state = Column(String)
    serial_number = Column(String)
    mac_ethernet = Column(String)
    mac_wifi = Column(String)


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class Task(Base):
    __tablename__ = "tasks"
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


api = "https://pymeshield.ebrehosting.asix2.iesmontsia.cat/api/"

# devuelve la url para poder hacer uso de la API


def returnUrl():
    return api


# Realiza la solicitud GET a la API
def get_api_data(url):
    try:
        response = ControlApi.metodoControlApi(api + url)
        data = json.loads(response.text)
        api_data = data
        engine.dispose()
        return api_data
    except:
        # Manejar excepciones de solicitud HTTP
        Notify(text="¡Error al conectarse al servidor!", snack_type="error").open()
    finally:
        engine.dispose()

# Método que recupera los datos de la API y recarga los datos en la aplicación
def Update():
    datatasks = get_api_data("all-data-kivy")
    datainventories = get_api_data("devicelist/")
    datacourses = get_api_data("course-user-data")
    databudgets = get_api_data("budgets-data")
    datareports = get_api_data("kivy/report")

    if datatasks is not None:
        dataTasks(datatasks)

    if databudgets is not None:
        dataBudgets(databudgets)

    if datareports is not None:
        dataReports(datareports)

    if datacourses is not None:
        dataCourses(datacourses)

    if datainventories is not None:
        dataInventory(datainventories)

    engine.dispose()
