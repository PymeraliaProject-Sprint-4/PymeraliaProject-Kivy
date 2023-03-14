from kivymd.uix.screen import MDScreen
import json
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones

from utils import load_kv

load_kv(__name__)

class ProfileScreen(MDScreen):

    def on_enter(self):
        #Recuperar token session
        self.session = JsonStore('session.json')
        print(self.session.get('token')['token'])

        with open('assets/Perfil.json', 'r') as f: #Aqui importem el arxiu json
            data = json.load(f)
        self.ids.name.text = data['nombre'] 
        self.ids.name1.text = data['nombre_de_usuario']
        self.ids.name2.text = data['correo']
        self.ids.name3.text = data['telefono']

if __name__ == "__main__": #per a arrancar el main
    ProfileScreen().run()
