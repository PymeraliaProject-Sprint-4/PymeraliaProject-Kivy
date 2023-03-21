from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget
from utils import load_kv
import requests
from utils import Notify

load_kv(__name__)


class QuestionaryScreen(MDScreen):
    def open(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        app.switch_screen('questionary')

    def on_enter(self):
        self.ids.informes.clear_widgets()
        # Al entrar, recuperamos los datos desde la API
        self.reports = self.get_reports()
        if self.reports is None:
            # If the API request failed, show an error message
            Notify(text="Error al recuperar los datos", snack_type='error').open()
            return
        self.update_list()

    def get_reports(self):
        url = "http://localhost/api/kivy/report"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as error:
            print(error)  # Logeamos el error
            return None

    def update_list(self):
        self.ids.informes.clear_widgets()
        for report in self.reports:
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
        app.switch_screen('details_questionary')
