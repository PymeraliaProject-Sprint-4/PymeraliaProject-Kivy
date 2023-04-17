from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from utils import load_kv
import json
import bcrypt

load_kv(__name__)

class QrScreen(MDScreen):

    def calc(self, instance):
        readQR = self.ids['qrlabel'].text
        readQR = readQR[2:]
        readQR = readQR[:-1]
        if (readQR != ''): #TO DO que compruebe también que es un número, si no que no entre
            self.dialog = MDDialog(
                text=readQR,
                buttons=[
                    MDFlatButton(
                        text="ver detalles",
                        theme_text_color="Custom",
                        on_release=lambda x: self.detailsQr(x, readQR)
                    )
                ]
            )
            self.dialog.open()
            
    #cierra el mensaje de la ventana emergente
    def detailsQr(self, instance, readQR):
        self.dialog.dismiss()
        app = MDApp.get_running_app()
        app.setRowDetails(readQR)
        self.manager.current = 'details_inventory'
        

    # método que nos lleva a la pantalla "home"
    def goHome(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        self.manager.current = 'Inicio'

