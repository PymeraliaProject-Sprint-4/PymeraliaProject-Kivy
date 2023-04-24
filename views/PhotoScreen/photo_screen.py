from kivymd.uix.screen import MDScreen
from kivy.uix.camera import Camera
from utils import load_kv
import base64

load_kv(__name__)

class PhotoScreen(MDScreen):
    camera = None
    def on_enter(self):
        self.camera = self.ids.camera_obj
    def onCameraClick(self):
        print('hello')
        self.camera.export_to_png('selfie.png')
        texture = self.camera.texture
        pixels = texture.pixels
        print(pixels)
        print(base64.b64encode(pixels))
