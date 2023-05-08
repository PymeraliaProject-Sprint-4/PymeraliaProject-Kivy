from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ThreeLineIconListItem
from utils import load_kv
import sqlite3

load_kv(__name__)


def get_data_sqlite():
    conn = sqlite3.connect("pymeshield.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")

    rows = cursor.fetchall()

    data = []

    for row in rows:
        data.append(
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
            }
        )

    data = data

    return data


class CourseScreen(MDScreen):
    def on_enter(self, *args):
        # Obtener la lista completa de cursos
        self.cursos_completos = self.get_cursos()
        self.mostrar_cursos(self.cursos_completos)

    def on_leave(self, *args):
        self.ids.courselist.clear_widgets()

    def get_cursos(self):
        data = get_data_sqlite()

        cursos = []
        for course in data:
            item = ThreeLineIconListItem(
                IconLeftWidget(
                    icon="book",
                ),
                text=f"Curso- {course['name']}",
                secondary_text=f"{course['description']}",
            )
            cursos.append(item)

        return cursos

    def buscar_curso(self, texto_busqueda):
        # Cancelar búsquedas previas
        if hasattr(self, "search_event"):
            self.search_event.cancel()

        # Añadir delay
        self.search_event = Clock.schedule_once(
            lambda dt: self.hacer_busqueda(texto_busqueda), 0.5
        )

    def hacer_busqueda(self, texto_busqueda):
        # Obtener la lista completa de cursos
        cursos = self.cursos_completos[:]

        # Filtrar los cursos según la cadena de búsqueda
        cursos_filtrados = []
        for curso in cursos:
            if (
                texto_busqueda.lower() in curso.text.lower()
                or texto_busqueda.lower() in curso.secondary_text.lower()
            ):
                cursos_filtrados.append(curso)

        # Mostrar los cursos filtrados
        self.mostrar_cursos(cursos_filtrados)

    def mostrar_cursos(self, cursos):
        # Limpiar widgets
        self.ids.courselist.clear_widgets()

        # Mostrar los cursos en la lista
        for curso in cursos:
            self.ids.courselist.add_widget(curso)
