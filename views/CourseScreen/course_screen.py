import requests
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import ThreeLineIconListItem
from kivy.clock import Clock
import sqlite3
from utils import load_kv
import json

API_URL = "http://localhost"  # Definimos la ruta para la api y la guardamos en una variable

load_kv(__name__)


class CourseScreen(MDScreen):

    def get_data_sqlite(self):
        conn = sqlite3.connect('pymeshield.db')

        cursor = conn.cursor()
    
        cursor.execute('SELECT * FROM courses')
        
        rows = cursor.fetchall()
        
        data = []
        
        for row in rows:
            data.append({
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'date': row[3]
            })

        self.data = data
        
        return self.data        
            
    def insert_data(self, data):
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


    def on_enter(self, *args):
        # Obtener la lista completa de cursos
        self.cursos_completos = self.get_cursos()
        self.mostrar_cursos(self.cursos_completos)

    def get_cursos(self):
        # Obtener la lista completa de cursos
        app = MDApp.get_running_app()
        ddbb = app.get_api_data('couser-user-data')
        self.insert_data(ddbb)
        data = self.get_data_sqlite()

        cursos = []
        for course in data:
            item = ThreeLineIconListItem(
                IconLeftWidget(
                    icon="book",
                ),
                text=f"Curso- {course['name']}",
                secondary_text=f"{course['description']}"
            )
            cursos.append(item)

        return cursos

    def buscar_curso(self, texto_busqueda):
        # Obtener la lista completa de cursos
        cursos = self.cursos_completos[:]

        # Filtrar los cursos según la cadena de búsqueda
        cursos_filtrados = []
        for curso in cursos:
            if texto_busqueda.lower() in curso.text.lower() or texto_busqueda.lower() in curso.secondary_text.lower():
                cursos_filtrados.append(curso)

        # Mostrar los cursos filtrados
        self.mostrar_cursos(cursos_filtrados)

    def mostrar_cursos(self, cursos):
        # Mostrar los cursos en la lista
        self.ids.list.clear_widgets()
        for curso in cursos:
            self.ids.list.add_widget(curso)
