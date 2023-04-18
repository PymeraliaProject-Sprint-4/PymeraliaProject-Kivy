from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, IconLeftWidget
from kivymd.uix.list import TwoLineIconListItem

from utils import load_kv
import json
import bcrypt

load_kv(__name__)

class InventoryScreen(MDScreen):
    def buscar(self, item):

        searchDevice = [search_field for search_field in self.datosDevices if (item.lower() in search_field['brand'].lower()) or (item.isdigit() and int(item) == search_field['id'])]
        
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

        app = MDApp.get_running_app()
        datosDevices = app.get_api_data('devicelist')
        self.datosDevices = datosDevices

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
        # app.switch_screen('details_inventory')  # mostrar detalles de la tarea.
        self.manager.current = "details_inventory"
        
    
    def open_camera(self, *args):
        app = MDApp.get_running_app()
        self.manager.current = "QR"
        