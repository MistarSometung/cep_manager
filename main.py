from kivy.app import App
from controller import Controle

class Main(App):
    def build(self):
        wg = Controle()
        
        

        return wg.sm 

Main().run()