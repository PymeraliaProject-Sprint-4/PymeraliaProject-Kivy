from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import Notify, load_kv
import json
import bcrypt

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
        email = self.ids.email.text
        password = self.ids.password.text
        with open("assets/users.json","rt") as users:
            users = json.load(users)
        
        for user in users:
            if user['email'] == email:
                # si encuentra el email hasheamos la contraseña
                salt = user['password'].encode('utf-8')
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                # si coinciden se hace login
                if hashed_password == user['password'].encode('utf-8'):
                    Notify(text="¡Bienvenido a Pymeshield!", snack_type='success').open()
                    app = MDApp.get_running_app()
                    app.switch_screen('dashboard')
            
        Notify(text="¡Usuario o contraseña incorrecta!", snack_type='error').open()
        app = MDApp.get_running_app()
        self.clear()