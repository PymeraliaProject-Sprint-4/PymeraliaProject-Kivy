from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv, Notify  # cargar ruta del script
from views.ReportScreen.report_screen import get_data_sqlite

load_kv(__name__)


class DetailsReportScreen(MDScreen):
    def index(self):
        self.manager.current = "Inicio"

    def goBack(self, screen):
        self.manager.current = screen

    def on_enter(self):
        try:
            # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
            app = MDApp.get_running_app()
            id_informe = app.rowPressed()
            data = get_data_sqlite()

            img2 = "assets/inprogress.gif"
            img3 = "assets/done.gif"

            id_informe = int(id_informe[8:])

            for i in data:
                if i["id"] == id_informe:
                    status = i["status"]
                    self.ids.estatext.text = f"{i['name']} - {status}"
                    if status == "pending":
                        self.ids.imagen.source = img2
                    elif status == "done":
                        self.ids.imagen.source = img3
                    break

        except Exception as e:
            # Handle any exceptions that may have occurred during the request.
            Notify(text="Error al recuperar los datos", snack_type="error").open()
