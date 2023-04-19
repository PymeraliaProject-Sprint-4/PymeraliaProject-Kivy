from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import Notify, load_kv
import requests
from kivy.storage.jsonstore import JsonStore # libreria para las sessiones
from updates import Update
from db import CreateDB

load_kv(__name__)

class LoginScreen(MDScreen):
    def open(self):
        app = MDApp.get_running_app()
        self.ids.email.focus = True
        app.switch_screen('login')

    def clear(self):
        self.ids.email.text = ""
        self.ids.password.text = ""

    def do_login(self):
        app = MDApp.get_running_app()
        self.session = JsonStore('session.json')
        email = self.ids.email.text
        password = self.ids.password.text

        # DE MOMENTO HASTA LA UNIFICACIÓN
        Notify(text="¡Bienvenido a Pymeshield!", snack_type='success').open()
        app.switch_screen('dashboard')

        # Envía la solicitud POST con los datos de email y password
        response = requests.post('http://localhost/api/loginPhone', data={'email': email, 'password': password})
        

        if response.status_code == 200:
            # Redireccionar al login si la respuesta del servidor es correcta
            Notify(text="¡Bienvenido a Pymeshield!", snack_type='success').open()
            app.switch_screen('dashboard')
            # Recuperamos el token de sessión, el company_id para poder filtrar y el tipo de usuario
            token = response.json().get('token')
            company_id = response.json().get('company_id')
            type = response.json().get('user_type')
            # print(response.json())
            # Guardamos el token, el company_id y el tipo de usuario en la session
            self.session.put('token',token=token)
            self.session.put('company_id', company_id=company_id)
            self.session.put('type', type=type)
            CreateDB()
            Update()

        else:
            # Si la respuesta es incorrecta, se muestra el mensaje de error
            Notify(text="¡Usuario o contraseña incorrecta!", snack_type='error').open()
            self.clear()
