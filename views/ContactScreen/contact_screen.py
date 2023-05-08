from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from utils import load_kv  # cargar ruta del script

load_kv(__name__)


class ContactScreen(MDScreen):
    def index(self):
        self.manager.current = "Inicio"

    def on_enter(self):
        self.ids.text1.text = f"Pymeralia (Consultoría tecnológica | Pymeralia)"
        self.ids.text2.text = f"Email: hola@pymeralia.com"
        self.ids.text3.text = f"Teléfono: 977 74 40 87"
        self.ids.text4.text = (
            f"Dirección: Av. dels Esports, 18, 43540 La Ràpita, Tarragona"
        )
        self.ids.text5.text = f"Página web: pymeralia.com"
