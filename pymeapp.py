from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock

class SplashScreen(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 2)
    def switch_to_home(self, dt):
        app = MDApp.get_running_app()
        app.switch_screen('login')

class ContentNavigationDrawer(MDScrollView):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Dashboard(MDScreen):
    pass

class PymeApp(MDApp):
    
    sm = None
    
    def build(self):
        if platform in ['win', 'linux', 'macosx']:
            #resolución más común móvil
            Window.size = (414, 750)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        self.icon = "assets/pymeshield_favicon.png"
        self.title ="Pymeshield"
        self.sm = self.root
        

    def switch_screen(self, screen_name='login'):
         self.sm.current = screen_name
         
   

if __name__ == '__main__':
    app = PymeApp()
    app.run()