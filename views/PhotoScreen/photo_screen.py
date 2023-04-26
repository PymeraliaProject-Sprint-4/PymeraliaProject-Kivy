from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
# from kivy.uix.camera import Camera
from utils import load_kv
import base64
from PIL import Image
import os
import requests

load_kv(__name__)

class PhotoScreen(MDScreen):
    camera = None
    def on_enter(self, *args):
        self.camera = self.ids.camera_obj
        self.app = MDApp.get_running_app()
        self.camera.play = True
        
    def on_leave(self, *args):
        self.camera.play = False

    def onCameraClick(self):
        print('hello')
        self.camera.export_to_png('selfie.png')
        filepath = os.path.join(self.app.user_data_dir, 'selfie.png')
        image = {"files": open(filepath, "rb")}
        response = requests.post(self.app.api + 'image', data={'id_device': 2}, files=image)
        print(response.status_code)
