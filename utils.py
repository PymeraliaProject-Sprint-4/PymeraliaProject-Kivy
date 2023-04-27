from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones
import os, requests

def load_kv(module_name):
    Builder.load_file(f"{os.path.join(*module_name.split('.'))}.kv")
    
class Notify(Snackbar):
    def __init__(self, **kwargs):
        text = kwargs.get('text', '')
        snack_type = kwargs.get('snack_type', 'success')
        bg_color = (.8, 0, 0, 1) if snack_type == 'error' else (0, .6, 0, 1)
        super().__init__(text=text,
                         bg_color=bg_color,
                         size_hint_x=(Window.width - (dp(10) * 2)) / Window.width,
                         snackbar_x="10dp",
                         snackbar_y="10dp"
                         )

class ControlApi():
    def metodoControlApi(direccion):
        #Recuperar token session
        session = JsonStore('session.json')
        session_token = session.get('token')['token']
        # Configurar la cabecera de la solicitud GET
        headers = {'Authorization': 'Bearer ' + session_token}
        # Realizar la solicitud GET a la API
        
        try:
            response = requests.get(direccion, headers=headers)
            return response  
        except requests.exceptions.RequestException as e:
            # Manejar excepciones de solicitud HTTP
            Notify(text="¡Error al conectarse al servidor!", snack_type='error').open()

# Clase que se encarga de las acciones que van a realizar los buscadores.
class SearchE4(MDTextField): 
    pass