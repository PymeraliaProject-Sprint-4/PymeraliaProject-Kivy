from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget
from utils import load_kv
import requests
from utils import Notify
import sqlite3

load_kv(__name__)

data = []

def get_data_sqlite():
    conn = sqlite3.connect('pymeshield.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM reports')
    
    rows = cursor.fetchall()
    
    data = []
    
    for row in rows:
        data.append({
        'id': row[0],
        'name': row[1],
        'status': row[2],
        'date': row[3]
        })

    data = data
    
    return data    

class QuestionaryScreen(MDScreen):
            
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('questionary')

    def on_enter(self):
        data = get_data_sqlite()
        self.ids.informes.clear_widgets()
        
        for report in data:
            self.ids.informes.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                        icon="clipboard-file-outline"
                    ),
                    id=f"informe-{report['id']}",
                    text=f"{report['name']}",
                    on_press=self.print
                )
            )

    def buscar_informe(self, query):
        if not self.reports:
            return

        # Limpiar la lista de informes antes de mostrar los resultados de búsqueda
        self.ids.informes.clear_widgets()
        # Verificar si el nombre del informe contiene la query
        filtered_reports = filter(
            lambda x: query.lower() in x['name'].lower(), self.reports)
        for report in filtered_reports:
            self.ids.informes.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                        icon="clipboard-file-outline"
                    ),
                    id=f"informe-{report['id']}",
                    text=f"{report['name']}",
                    on_press=self.print
                )
            )

    def print(self, row):
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        self.manager.current="details_questionary"
