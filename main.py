import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import IconLeftWidget
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.textinput import TextInput


class SearchBar(TextInput):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):

        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MyApp(MDApp):

    def build(self):
        self.title = "PymeShield"
        Window.size = (400, 600)
        self.sm = self.root
        return Builder.load_file("main2.kv")

    def on_start(self):
        with open("JSON/course.json", "rt") as json_file_course:
            data_course = json.load(json_file_course)

        for i in data_course:
            self.root.ids.cursos.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                        icon="book"
                    ),
                    id=f"curso-{i['id']}",
                    text=f"{i['curso']}"
                )
            )

        self.cursos_list = self.root.ids.cursos

        with open("JSON/tasks.json", "rt") as json_file_tasks:
            data_tasks = json.load(json_file_tasks)

        for i in data_tasks:
            self.root.ids.actividades.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                        icon="clipboard-check"
                    ),
                    id=f"tarea-{i['id']}",
                    text=f"{i['tarea']}"
                )
            )  

        self.actividades_list = self.root.ids.actividades

    def on_search_text_changed(self, search_text):
        self.filter_list_course(search_text)
        self.filter_list_tasks(search_text)

    def filter_list_course(self, search_text):
        self.cursos_list.clear_widgets()
        with open('JSON/course.json') as course:
            data_course = json.load(course)
        filtered_list = [course for course in data_course if search_text.lower() in course['curso'].lower()]
        for course in filtered_list:
            self.cursos_list.add_widget(
                OneLineListItem(text=f"Curso: {course['curso']}", on_press=self.print_course, id=str(course['id']))
            )

    def print_course(self, row):
        print(f"{row.id}")

    def filter_list_tasks(self, search_text):
        self.actividades_list.clear_widgets()
        with open('JSON/tasks.json') as tasks:
            data_tasks = json.load(tasks)
        filtered_list = [tasks for tasks in data_tasks if search_text.lower() in tasks['tarea'].lower()]
        for tasks in filtered_list:
            self.actividades_list.add_widget(
                OneLineListItem(text=f"Actividad: {tasks['tarea']}", on_press=self.print_task, id=str(tasks['id']))
            )

    def print_task(self, row):
        print(f"{row.id}")


if __name__ == "__main__":
    MyApp().run()
