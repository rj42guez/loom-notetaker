import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget 

# from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os

class FileChoose(Popup):
    load = ObjectProperty()


class MyGridLayout(Widget):
    file_path = StringProperty("No file chosen")
    text_input = ObjectProperty()
    popup = ObjectProperty()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.text_input.text = stream.read()
        self.popup.dismiss()
    
    def open(self):
        Tk().withdraw()
        path = filedialog.askopenfilename()
        if path:
            file = open(path, 'r')
            contents = file.read()
            file.close()
            self.ids.text_input.text = contents

    def saveAs(self):
        Tk().withdraw()
        path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if path:
            file = open(path, 'w')
            file.write(self.ids.text_input.text)



class MyApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()