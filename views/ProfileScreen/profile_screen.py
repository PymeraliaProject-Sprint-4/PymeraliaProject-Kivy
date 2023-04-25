from kivymd.uix.screen import MDScreen
import json
from kivy.storage.jsonstore import JsonStore  # libreria para las sessiones
import requests
import os  # importa biblioteca os para trabajar con rutas y archivos
from utils import ControlApi, Notify
from updates import returnUrl
import sqlite3

from utils import load_kv

load_kv(__name__)


class ProfileScreen(MDScreen):

    def on_enter(self):
        api = returnUrl()
        # Realizar la solicitud GET a la API
        response = ControlApi.metodoControlApi(api + 'user')
        print(response)
        # Procesar la respuesta
        try:
            if response.status_code == 200:
                data = response.json()
                self.ids.name.text = data['name']
                self.ids.name1.text = data['nick_name']
                self.ids.name2.text = data['email']
                self.ids.name3.text = data['phone']

                # Crear conexión con la base de datos
                conn = sqlite3.connect('pymeshield.db')

                # Seleccionar la tabla correspondiente
                
                cur = conn.cursor()
                table_name = 'users'  # Reemplazar con el nombre de la tabla correspondiente
                cur.execute(f"DELETE FROM {table_name}") #elimina los datos de la tabla users
                cur.execute(f"INSERT INTO {table_name} (name, nick_name, email, phone) VALUES (?, ?, ?, ?)",
                            (data['name'], data['nick_name'], data['email'], data['phone']))

                # Guardar los cambios y cerrar la conexión
                conn.commit()
                conn.close()

                # Comprueba si existe una carpeta y si no existe la crea en la ruta que le indicamos
                image_folder = "./PymeraliaProject-Kivy/profile_images"
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)

                # comprueba si el dato que recoge existe o no
                if data['profile_image'] is not None:
                    image_url = "http://localhost/img/profile_images/" + \
                        data['profile_image']  # guarda la url donde se encuentra la imagen
                    # os.path.join() une varias rutas, os.getcwd() obtiene el directorio actual
                    image_path = os.path.join(
                        os.getcwd(), "./PymeraliaProject-Kivy/profile_images", data['profile_image'])
                    # solicitud HTTP GET a la url
                    response = requests.get(image_url)
                    # abre el archivo de forma binaria para no perder memoria
                    with open(image_path, "wb") as f:
                        # se escribe el archivo en la ruta especificada
                        f.write(response.content)
                    self.ids.imagen.source = image_path
                else:
                    # imagen que carga por defecto si no encuentra imagen
                    self.ids.imagen.source = "./assets/default_profile.jpg"

            else:
                # Si la respuesta es incorrecta, se muestra el mensaje de error
                Notify(text="¡Error al recuperar los datos!",
                       snack_type='error').open()
        except:
            Notify(text="¡Error con el servidor!", snack_type='error').open()


if __name__ == "__main__":  # per a arrancar el main
    ProfileScreen().run()
