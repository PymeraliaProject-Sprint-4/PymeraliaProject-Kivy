from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.screen import MDScreen
from utils import load_kv
import sqlite3

load_kv(__name__)

data = []


def get_data_sqlite():
    conn = sqlite3.connect("pymeshield.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports")

    rows = cursor.fetchall()

    data = []

    for row in rows:
        data.append(
            {
                "id": row[0],
                "name": row[1],
                "status": row[2],
            }
        )

    data = data

    return data


class ReportScreen(MDScreen):
    reports = []

    def open(self):
        self.manager.current = "report"

    def on_leave(self, *args):
        self.ids.informes.clear_widgets()

    def on_enter(self):
        data = get_data_sqlite()

        for report in data:
            self.reports.append(report)
            self.ids.informes.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(icon="clipboard-file-outline"),
                    id=f"informe-{report['id']}",
                    text=f"{report['name']}",
                    on_press=self.print,
                )
            )

    def buscar_informe(self, query):
        if not self.reports:
            return
        # Cancelar búsquedas previas
        if hasattr(self, "search_event"):
            self.search_event.cancel()

        # Añadir delay
        self.search_event = Clock.schedule_once(
            lambda dt: self.hacer_busqueda(query), 0.5
        )

    def hacer_busqueda(self, query):
        # Limpiar la lista de informes antes de mostrar los resultados de búsqueda
        self.ids.informes.clear_widgets()
        # Verificar si el nombre del informe contiene la query
        filtered_reports = filter(
            lambda x: query.lower() in x["name"].lower(), self.reports
        )
        for report in filtered_reports:
            self.ids.informes.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(icon="clipboard-file-outline"),
                    id=f"informe-{report['id']}",
                    text=f"{report['name']}",
                    on_press=self.print,
                )
            )

    def print(self, row):
        app = MDApp.get_running_app()
        app.setRowDetails(row.id)
        self.manager.current = "details_report"
