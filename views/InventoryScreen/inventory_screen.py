from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IconLeftWidget, TwoLineIconListItem
from utils import load_kv
import sqlite3

load_kv(__name__)

data = []
def get_data_sqlite():
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM inventories')
    
    rows = cursor.fetchall()
    
    data = []
    
    for row in rows:
        data.append({
        'id': row[0],
        'brand': row[1],
        'model': row[2],
        'state': row[3],
        'serial_number': row[4],
        'mac_ethernet': row[5],
        'mac_wifi': row[6],
        'description': row[7]
        })

    data = data
    return data


class InventoryScreen(MDScreen):
    def buscar(self, item):
        data = get_data_sqlite()
        
        searchDevice = [search_field for search_field in data if (item.lower() in search_field['brand'].lower()) or (item.lower() in search_field['state'].lower()) or (item.isdigit() and int(item) == search_field['id'])]
        
        #actualitzar la llista filtrada
        searchDeviceList = self.ids.listaDispositivos
        searchDeviceList.clear_widgets()
        
        for result in searchDevice:
            searchDeviceList.add_widget(
                TwoLineIconListItem(
                    IconLeftWidget(
                            icon="laptop"
                        ), 
                    
                    text=f"Dispositiu: {result['brand']} {result['model']}",
                    secondary_text=f"Estat dispositiu: {result['state']}",
                    id = f"{result['id']}",
                    on_press=self.detalles
                )
            )

    
    def on_enter(self, *args):
        self.ids.listaDispositivos.clear_widgets()

        datosDevices = get_data_sqlite()

        # Crear el layout principal
        layout = MDBoxLayout()

        for result in datosDevices:
            item = TwoLineIconListItem(
                IconLeftWidget(
                    icon="laptop",
                ),
                text=f"Dispositiu: {result['brand']} {result['model']}",
                secondary_text=f"Estat dispositiu: {result['state']}",
                id = f"{result['id']}",
                on_press=self.detalles
            )

            #Pinta los widgets de cada dispositivo en una lista
            self.ids.listaDispositivos.add_widget(item)

        # retornem la llista de dispositius
        return layout
    
    def detalles(self, row):  # inicializamos una función con el parametro row
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        self.manager.current = "details_inventory"
        
    
    def open_camera(self, *args):
        self.manager.current = "QR"
        