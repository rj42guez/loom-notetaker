import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget  
from pathlib import Path
from kivy.lang import Builder
from kivy.uix.button import Button

import datetime
import os


#class LoadDialog(FloatLayout):
#    load = ObjectProperty(None)
#    cancel = ObjectProperty(None)

class FileChooser(BoxLayout):
    def file_fire_select(self, *args):
        file_selected = args[1][0]
        created_date = Path(file_selected)
        f = open(created_date)
        self.label.text = f.read()


class MyGridLayout(Widget):
    
    #def selected(self, filename):
    #    try:

    #def selected2(self, *args):
    #    file_selected = args[1][0]
    #    created_date = Path(file_selected)
    #    f = open(created_date)
    #    self.label.text = f.read()

    def btn(self):
        show_popup()
    
    def updateText(self):
        self.text.text = content
    

content = " "

class P(BoxLayout):
    def file_fire_select(self, *args):
        file_selected = args[1][0]
        created_date = Path(file_selected)
        f = open(created_date)
        content = f.read()
        print(content)
        
        
class MyApp(App):
    def build(self):
        return MyGridLayout()

def show_popup():
    popupContent = P()
    popupWindow = Popup(title="Open File", content = popupContent)
    popupContent.bind(on_press=popupWindow.dismiss)
    popupWindow.open()

if __name__ == "__main__":
    MyApp().run()