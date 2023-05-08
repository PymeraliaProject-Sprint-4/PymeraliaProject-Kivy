from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv, Notify

load_kv(__name__)


class QrScreen(MDScreen):
    contador = False

    # Método que se ejecuta al entrar en la pantalla QR
    def on_enter(self):
        self.contador = False

    # Método que tira hacia la pantalla anterior
    def goBack(self, screen):
        self.manager.current = screen

    # Método que lee el código QR
    def leerQR(self, instance):
        readQR = self.ids["qrlabel"].text
        readQR = readQR[2:-1]

        if self.contador == False:
            if not readQR.isnumeric():
                Notify(text="¡QR no válido!", snack_type="error").open()
            else:
                self.detailsQr(None, readQR)
                Notify(text="¡QR leído correctamente!", snack_type="success").open()
                self.contador = True

    # Método que nos dirige a la pantalla de detalles del dispositivo

    def detailsQr(self, instance, readQR):
        app = MDApp.get_running_app()
        app.setRowDetails(readQR)
        self.manager.current = "details_inventory"

    # Método que nos lleva a la pantalla "home"
    def goHome(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        self.manager.current = "Inicio"
