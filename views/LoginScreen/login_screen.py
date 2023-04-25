from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import Notify, load_kv
import requests
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones
from updates import Update
from db import CreateDB
import os
import atexit

load_kv(__name__)

class LoginScreen(MDScreen):
    def on_enter(self, *args):
        print('[*ALEIX*]: On enter login')
        
    def open(self):
        app = MDApp.get_running_app()
        self.ids.email.focus = True
        app.switch_screen('login')

    #  Método que elimina los archivos session.json y pymeshield.db
    def borrarSesion():
        archivoSesion = './session.json'
        archivoBBDD = './pymeshield.db'

        if os.path.exists(archivoSesion):
            os.remove(archivoSesion)
        if os.path.exists(archivoBBDD):
            os.remove(archivoBBDD) 

    # Método que cierra sesión
    def logout():
        app = MDApp.get_running_app()
        app.switch_screen('login')
        LoginScreen.borrarSesion()
        
        
    
    #acción que ejecuta el método borrar sesión si se cierra el aplicativo de manera forzosa
    atexit.register(borrarSesion)

    def clear(self):
        self.ids.email.text = ""
        self.ids.password.text = ""

    def do_login(self):
        app = MDApp.get_running_app()
        self.session = JsonStore('session.json')
        email = self.ids.email.text
        password = self.ids.password.text
        
        try:
            # Envía la solicitud POST con los datos de email y password
            response = requests.post('http://localhost/api/loginPhone', data={'email': email, 'password': password})
            print(response)
            if response.status_code == 200:
                # Redireccionar al login si la respuesta del servidor es correcta
                Notify(text="¡Bienvenido a Pymeshield!", snack_type='success').open()
                #limpia los inputs para que queden vacios al hacer logout
                self.clear()
                app.switch_screen('dashboard')
                # Recuperamos el token de sessión, el company_id para poder filtrar y el tipo de usuario
                token = response.json().get('token')
                company_id = response.json().get('company_id')
                tipo = response.json().get('user_type')
                # Guardamos el token, el company_id y el tipo de usuario en la session
                self.session.put('token',token=token)
                self.session.put('company_id', company_id=company_id)
                self.session.put('type', type=tipo)
                CreateDB()
                Update()
            
            #error para el servicio caído
            elif response.status_code == 404:
                # Si la respuesta es incorrecta, se muestra el mensaje de error
                Notify(text="¡Servicio No Disponible!", snack_type='error').open()
                self.clear()
                
            else:
                # Si la respuesta es incorrecta, se muestra el mensaje de error
                Notify(text="¡Usuario o contraseña incorrecta!", snack_type='error').open()
                self.clear()

        except requests.exceptions.RequestException as e:
            # Manejar excepciones de solicitud HTTP
            Notify(text="¡Error al conectarse al servidor!", snack_type='error').open()
            
            