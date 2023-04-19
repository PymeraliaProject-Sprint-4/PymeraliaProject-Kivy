from kivymd.uix.screen import MDScreen
import json
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones
import requests
import os #importa biblioteca os para trabajar con rutas y archivos

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
        response = requests.get('http://192.168.224.241/api/user', headers=headers)
        
        

        # Procesar la respuesta
        if response.status_code == 200:
            data = response.json()
            self.ids.name.text = data['name'] 
            self.ids.name1.text = data['nick_name']
            self.ids.name2.text = data['email']
            self.ids.name3.text = data['phone']
        
            # Comprueba si existe una carpeta y si no existe la crea en la ruta que le indicamos
            image_folder = "./PymeraliaProject-Kivy/profile_images"
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)

            #comprueba si el dato que recoge existe o no
            if data['profile_image'] is not None:
                image_url = "http://192.168.224.241/img/profile_images/" + data['profile_image'] #guarda la url donde se encuentra la imagen
                image_path = os.path.join(os.getcwd(), "./PymeraliaProject-Kivy/profile_images", data['profile_image']) #os.path.join() une varias rutas, os.getcwd() obtiene el directorio actual
                response = requests.get(image_url) #solicitud HTTP GET a la url
                with open(image_path, "wb") as f: #abre el archivo de forma binaria para no perder memoria
                    f.write(response.content) #se escribe el archivo en la ruta especificada
                self.ids.imagen.source = image_path 
            else:
                self.ids.imagen.source = "./assets/default_profile.jpg" #imagen que carga por defecto si no encuentra imagen
                
        else:
            print("You don't have access")

if __name__ == "__main__": #per a arrancar el main
    ProfileScreen().run()
