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
        text = self.ids['qrlabel'].text
        text = text[2:]
        text = text[:-1]
        print(text)
        if (text != ''):
            MDDialog(
                text=text,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom"
                    )
                ]
            )
            self.dialog.open()
            
    #cierra el mensaje de la ventana emergente
    def close_dialog(self, instance):
        self.dialog.dismiss()

    # método que nos lleva a la pantalla "home"
    def goHome(self):
        # Variable que utilizaremos para acceder a la applicacion que esta ejecutada.
        app = MDApp.get_running_app()
        self.manager.current = 'Inicio'

