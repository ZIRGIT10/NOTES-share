from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button  import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.lang.builder import Builder
from kivy.uix.anchorlayout import AnchorLayout
import  webbrowser
import pandas as pd
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor=(1,1,1,1)

def BCA5th(username):
    file_id ='1JUqVjDriK1vA6KrOCc9lU_uJP9GdyH4W'
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv')
    search_value = username 
    column_to_search = 'Enrollment_No' 
    result = df[df[column_to_search] == search_value]
    login = result[column_to_search].values[0]
    return login


class Home(Screen):
    pass

class firstscreen(Screen):
    pass

class PythonScreen(Screen):
    pass     


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.username_input = TextInput(hint_text='Enrolment', multiline=False)
        login_button = Button(text='Login', on_press=self.check_credentials,background_color=(19/225,30/225, 176/225,1))#,background_color_down=(5/225, 9/225, 61/225,1))

        layout.add_widget(Label(text='Login Page', font_size=40,bold=True,color=(0, 0, 0, 1)))
        layout.add_widget(self.username_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def check_credentials(self, instance):
        username = self.username_input.text
        
        login = BCA5th(username)
            

        if username == login:
            print('Login successful')
            self.manager.current = 'sec'
        else:
            print('Invalid credentials') 
            
          
class secscreen(Screen):
     pass
class BCAsemfst(Screen):
    pass
class mathsfst(Screen):
    pass
class c_prog(Screen):
    pass

class cdffst(Screen):
    pass
class communication(Screen):
    pass
class pcpack(Screen):
    pass

class BCAsemsec(Screen):
    pass
class BCAsemthr(Screen):
    pass
class BCAsemfor(Screen):
    pass
class BCAsemfiv(Screen):
    pass
class BCAsemsix(Screen):
    pass
        

class NotesApp(App):
    sm = ScreenManager()
    sm.add_widget(secscreen(name = "sec"))
    sm.add_widget(Login(name="log"))
    sm.add_widget(c_prog(name="cprog"))
    
    def cunit1(self):
        webbrowser.open('https://drive.google.com/file/d/1ejPDpegJT8RC6SdgnKG0BFof9LMxArAZ/view?usp=drive_link')
    
    def on_start(self):
        # Set the app to fullscreen
        self.root_window.fullscreen = 'auto'
            
NotesApp().run()

    

