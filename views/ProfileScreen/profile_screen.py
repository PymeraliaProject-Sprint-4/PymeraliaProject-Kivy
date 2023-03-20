from kivymd.uix.screen import MDScreen
import json
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones
import requests

from utils import load_kv

load_kv(__name__)

class ProfileScreen(MDScreen):

    def on_enter(self):
        #Recuperar token session
        self.session = JsonStore('session.json')
        session_token = self.session.get('token')['token']

        # Configurar la cabecera de la solicitud GET
        headers = {'Authorization': 'Bearer ' + session_token}

        # Realizar la solicitud GET a la API
        response = requests.get('http://localhost/api/user', headers=headers)

        # Procesar la respuesta
        if response.status_code == 200:
            data = response.json()
            self.ids.name.text = data['name'] 
            self.ids.name1.text = data['nick_name']
            self.ids.name2.text = data['email']
            self.ids.name3.text = data['phone']
        else:
            print("You don't have access")

if __name__ == "__main__": #per a arrancar el main
    ProfileScreen().run()
