from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget
from utils import load_kv
import requests
from utils import Notify
import sqlite3

load_kv(__name__)


class QuestionaryScreen(MDScreen):
    def get_data_sqlite(self):
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

        self.data = data
        
        return self.data        
            
    def insert_data(self, data):
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
    
    
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('questionary')

    def on_enter(self):
        app = MDApp.get_running_app()
        ddbb = app.get_api_data('kivy/report')
        self.insert_data(ddbb)
        data = self.get_data_sqlite()
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
