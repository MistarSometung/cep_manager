from kivy.uix.screenmanager import ScreenManager
from janelas import first_screen
from janelas import second_screen
from janelas import control_first

class Controle(object):
    def __init__(self):

        self.sm = ScreenManager()
        
        self.sm.add_widget(first_screen.first_screen)
        self.sm.add_widget(second_screen.second_screen)

        control_first.Funcoes()

        first_screen.bt_ok.bind(on_release = lambda x: self.ir())
        second_screen.bt_teste.bind(on_release = lambda x: self.voltar())
        
        pass

    def ir(self):
        if first_screen.spin.text != 'Clientes':
            first_screen.lb_resumo.text=''
            self.sm.current='segunda'
        else:
            first_screen.lb_resumo.text='Selecione um cliente.'
    
    def voltar(self):
        self.sm.current='primeira'
        pass