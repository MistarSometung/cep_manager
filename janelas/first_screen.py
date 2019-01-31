from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy. uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton

from kivy.graphics import Color, Rectangle

import database as db

radio_bt = None

# Criação dos box

layout_pai = BoxLayout(orientation = 'vertical') # Box que recebe todos os box

box_label = BoxLayout() # Box que recebe a Label de título
box_label.size_hint=1,0.2

box_meio = BoxLayout(orientation = 'vertical') # Box que recebe o boxgrid dos radioButtom e o box do spin

box_resumo =  BoxLayout(orientation ='vertical') # Recebe a Label que mostrará o resumo do cliente selecionado

box_check = GridLayout() # Agrupa os radioButtom
box_check.cols=3
box_check.size_hint= 1,0.5

box_spin = BoxLayout() # Box do spin
box_spin.size_hint = 1,0.5

box_bt = BoxLayout() # Box dos botões
box_bt.size_hint = 1,0.37


# Label título ========================================


label = Label()
label.size_hint=0.5,1.5
label.text='Gerenciador de clientes e pedidos'


# Label resumo ========================================

lb_resumo = Label()


""" Armazenar os valores no Spinner"""

spin = Spinner()
spin.size_hint= 0.2,0.5
spin.pos_hint={'top':0.5}
spin.text='Clientes'


lb_cidade = Label()
lb_nuped = Label()
lb_data = Label()
lb_valor = Label()

""" --------------------------------------------------------------------------"""

# Botãos ====================================

size_bt = [0.5 , 1]

bt_ok = Button()
bt_ok.size_hint= size_bt
bt_ok.text='Confirmar'
bt_ok.disabled=True

bt_inserir = Button()
bt_inserir.size_hint= size_bt
bt_inserir.text='Novo'

bt_resumo = Button()
bt_resumo.size_hint = size_bt
bt_resumo.text='Detalhar'
#====================================================

# Box do Checkbox

size = 16

ch_plastico = CheckBox()
ch_plastico.group=True

lb_plastico = Label()
lb_plastico.text='Plástico'
lb_plastico.halign='right'
lb_plastico.font_size = size

ch_construcao = CheckBox()
ch_construcao.group=True

lb_construcao = Label()
lb_construcao.text='Construção'
lb_construcao.font_size = size

ch_tecido = CheckBox()
ch_tecido.group=True

lb_tecido = Label()
lb_tecido.text='Tecido'
lb_tecido.font_size = size


# Criação do PopUp  ======================================
pop_layout = BoxLayout(orientation = 'vertical')
pop_tg = BoxLayout()

txt_nome = TextInput()
txt_nome.multiline=False
txt_nome.hint_text='Nome'

txt_cidade = TextInput()
txt_cidade.multiline=False
txt_cidade.hint_text='Cidade'

txt_numpedido = TextInput()
txt_numpedido.multiline=False
txt_numpedido.hint_text='Número do pedido'

txt_pedido = TextInput()
txt_pedido.hint_text='Itens do pedido'

txt_valor = TextInput()
txt_valor.multiline=False
txt_valor.hint_text='Valor (exemplo: 1,99)'




bt_pop = Button(text='Ok')

pop_layout.add_widget(txt_nome)
pop_layout.add_widget(txt_cidade)
pop_layout.add_widget(txt_numpedido)
pop_layout.add_widget(txt_pedido)
pop_layout.add_widget(txt_valor)
pop_layout.add_widget(bt_pop)

pop = Popup()
pop.size_hint = 0.8, 0.7
pop.title='Novo registro'
pop.content = pop_layout
#=========================================================


# addWidgets dos box
box_label.add_widget(label)
box_resumo.add_widget(lb_resumo)
box_resumo.add_widget(lb_cidade)
box_resumo.add_widget(lb_nuped)
box_resumo.add_widget(lb_data)
box_resumo.add_widget(lb_valor)

box_meio.add_widget(box_check)

box_check.add_widget(ch_plastico)
box_check.add_widget(ch_construcao)
box_check.add_widget(ch_tecido)
box_check.add_widget(lb_plastico)
box_check.add_widget(lb_construcao)
box_check.add_widget(lb_tecido)

box_meio.add_widget(box_spin)

box_meio.add_widget(box_resumo)

box_spin.add_widget(spin)

#box_bt.add_widget(bt_ok)
box_bt.add_widget(bt_resumo)
box_bt.add_widget(bt_inserir)

layout_pai.add_widget(box_label)
layout_pai.add_widget(box_meio)
layout_pai.add_widget(box_bt)


#==========================================================

# TELA
first_screen = Screen()

first_screen.add_widget(layout_pai)

first_screen.name='primeira'

# Cria as tabelas com o nome dos RadioButtom
x = [lb_construcao.text, lb_plastico.text, lb_tecido.text]

db.Create(x)


def cor(posi, tam):
    with label.canvas:
        Color(0,0,1,0.25)
        Rectangle(pos = posi, size = tam)



