from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from utils import load_kv, Notify
import json
import bcrypt

load_kv(__name__)


class QrScreen(MDScreen):

    contador = False
    
    def on_enter(self):
        self.contador = False
        
    def leerQR(self, instance):
        readQR = self.ids['qrlabel'].text
        readQR = readQR[2:-1]

        if (self.contador == False):
            if not readQR.isnumeric():
                Notify(text="¡QR no válido!", snack_type='error').open()
            else:
                self.detailsQr(None, readQR)
                Notify(text="¡QR leído correctamente!",snack_type='success').open()
                self.contador = True
                  

    # cierra el mensaje de la ventana emergente y nos dirige a la pantalla de detalles del dispositivo
    def detailsQr(self, instance, readQR):
        # self.dialog.dismiss()
        app = MDApp.get_running_app()
        app.setRowDetails(readQR)
        self.manager.current = 'details_inventory'

    # método que nos lleva a la pantalla "home"

    def goHome(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        self.manager.current = 'Inicio'
