from janelas import first_screen
from janelas import second_screen
import database as db
import time

class Funcoes(object):
    def __init__(self):

        self.tempo = time.localtime()

        first_screen.bt_inserir.bind(on_release = lambda x: self.inserir())
        first_screen.bt_pop.bind(on_release = lambda x: self.salvar_cliente()) # Botão que confirma a o registro de Novo cliente

        first_screen.spin.bind(on_release = lambda x: self.auto_spin())

        first_screen.bt_resumo.bind(on_release = lambda x: self.resumo())

        pass


    # Função que cria um registro para um cliente no banco de dados
    # de acordo com a tabela selecionada pelo RadioButtom
    # sendo ativado pelo botão OK no Popup
    def salvar_cliente(self):
        var = []
        
        nome = first_screen.txt_nome.text

        verificar = db.busca_spin(first_screen.lb_plastico.text)

        for x in verificar:
            for z in x:
                var.append(z)

        if nome != '' and first_screen.ch_plastico.active == True:
            tab = first_screen.lb_plastico.text
            nomereg = first_screen.txt_nome.text
            cidade = first_screen.txt_cidade.text 
            nupedido = first_screen.txt_numpedido.text
            item = first_screen.txt_pedido.text
            valor = first_screen.txt_valor.text
            dia = self.tempo[2]
            mes = self.tempo[1]
            ano = self.tempo[0]
            
            db.inserir(tab, nomereg, cidade, nupedido, item, valor, dia, mes, ano)

            first_screen.lb_resumo.text = nome + ' foi registrado com sucesso!'

            first_screen.txt_nome.text=''
            first_screen.txt_cidade.text=''
            first_screen.txt_numpedido.text=''
            first_screen.txt_pedido.text=''
            first_screen.txt_valor.text=''

            first_screen.pop.dismiss()
            

        elif nome != '' and first_screen.ch_construcao.active == True:
            tab = first_screen.lb_construcao.text
            nomereg = first_screen.txt_nome.text
            cidade = first_screen.txt_cidade.text 
            nupedido = first_screen.txt_numpedido.text
            item = first_screen.txt_pedido.text
            valor = first_screen.txt_valor.text
            dia = self.tempo[2]
            mes = self.tempo[1]
            ano = self.tempo[0]
            
            db.inserir(tab, nomereg, cidade, nupedido, item, valor, dia, mes, ano)

            first_screen.lb_resumo.text = nome + ' foi registrado com sucesso!'

            first_screen.txt_nome.text=''
            first_screen.txt_cidade.text=''
            first_screen.txt_numpedido.text=''
            first_screen.txt_pedido.text=''
            first_screen.txt_valor.text=''

            first_screen.pop.dismiss()

        elif nome != '' and first_screen.ch_tecido.active == True:
            tab = first_screen.lb_tecido.text
            nomereg = first_screen.txt_nome.text
            cidade = first_screen.txt_cidade.text 
            nupedido = first_screen.txt_numpedido.text
            item = first_screen.txt_pedido.text
            valor = first_screen.txt_valor.text
            dia = self.tempo[2]
            mes = self.tempo[1]
            ano = self.tempo[0]
            
            db.inserir(tab, nomereg, cidade, nupedido, item, valor, dia, mes, ano)

            first_screen.lb_resumo.text = nome + ' foi registrado com sucesso!'

            first_screen.txt_nome.text=''
            first_screen.txt_cidade.text=''
            first_screen.txt_numpedido.text=''
            first_screen.txt_pedido.text=''
            first_screen.txt_valor.text=''

            first_screen.pop.dismiss()
        else:
            pass    

    # Atualiza as opções do Spinner consultando o banco de dados
    # ao pressionar o botão do spinner
    def auto_spin(self):
        val_spin = []
        if first_screen.ch_plastico.active == True:
            for x in db.busca_spin(first_screen.lb_plastico.text):
                for z in x:
                    val_spin.append(z)
            first_screen.spin.values = val_spin
        
        elif first_screen.ch_construcao.active == True:
            for x in db.busca_spin(first_screen.lb_construcao.text):
                for z in x:
                    val_spin.append(z)
            first_screen.spin.values = val_spin

        elif first_screen.ch_tecido.active == True:
            for x in db.busca_spin(first_screen.lb_tecido.text):
                for z in x:
                    val_spin.append(z)
            first_screen.spin.values = val_spin


    # Abre o Popup para inserir novos registros
    def inserir(self):
        
        f_city = []
        plastico = first_screen.ch_plastico.active
        construcao = first_screen.ch_construcao.active
        tecido = first_screen.ch_tecido.active

        if plastico == True and first_screen.spin.text != 'Clientes':
            try:
                city = db.buscar_cidade(first_screen.lb_plastico.text, first_screen.spin.text)
                for x in city:
                    for z in x:
                        f_city.append(z)
                first_screen.txt_nome.text = first_screen.spin.text
                first_screen.txt_cidade.text=f_city[-1]
                first_screen.pop.open()
            except:
                first_screen.txt_nome.text = ''
                first_screen.txt_cidade.text=''
                first_screen.pop.open()

        elif construcao == True and first_screen.spin.text != 'Clientes':
            try:
                city = db.buscar_cidade(first_screen.lb_construcao.text, first_screen.spin.text)
                for x in city:
                    for z in x:
                        f_city.append(z)
                first_screen.txt_nome.text = first_screen.spin.text
                first_screen.txt_cidade.text=f_city[-1]
                first_screen.pop.open()
            except:
                first_screen.txt_nome.text = ''
                first_screen.txt_cidade.text=''
                first_screen.pop.open()

        elif tecido == True and first_screen.spin.text != 'Clientes':
            try:
                city = db.buscar_cidade(first_screen.lb_tecido.text, first_screen.spin.text)
                for x in city:
                    for z in x:
                        f_city.append(z)
                first_screen.txt_nome.text = first_screen.spin.text
                first_screen.txt_cidade.text=f_city[-1]
                first_screen.pop.open()
            except:
                first_screen.txt_nome.text = ''
                first_screen.txt_cidade.text=''
                first_screen.pop.open()

        
        elif plastico == False and construcao == False and tecido == False:
            first_screen.lb_resumo.text_size = [int(first_screen.lb_resumo.size[0]-50), None]
            first_screen.lb_resumo.text= 'Selecione uma das três categorias acima para registrar um novo cliente.'
        
        else:
            first_screen.pop.open()

    def resumo(self):

        res = []

        if first_screen.ch_plastico.active == True:
            try:
                reg = db.brief(first_screen.lb_plastico.text, first_screen.spin.text)
                for x in reg:
                    for z in x:
                        res.append(z)
                first_screen.lb_resumo.text = 'Nome : ' + res[1]
                first_screen.lb_cidade.text = 'Cidade: ' + res[2]
                first_screen.lb_nuped.text = 'Número do pedido: ' + str(res[3])
                first_screen.lb_data.text = 'Último pedido: ' + str(res[6]) + '/'+ str(res[7])+'/'+ str(res[8])
                first_screen.lb_valor.text = 'Valor: R$ ' + str(res[5])
                print(res)
            except:
                pass
        
        elif first_screen.ch_construcao.active == True:
            try:
                reg = db.brief(first_screen.lb_construcao.text, first_screen.spin.text)
                for x in reg:
                    for z in x:
                        res.append(z)
                first_screen.lb_resumo.text = 'Nome : ' + res[1]
                first_screen.lb_cidade.text = 'Cidade: ' + res[2]
                first_screen.lb_nuped.text = 'Número do pedido: ' + str(res[3])
                first_screen.lb_data.text = 'Último pedido: ' + str(res[6]) + '/'+ str(res[7])+'/'+ str(res[8])
                first_screen.lb_valor.text = 'Valor: R$ ' + str(res[5])
            except:
                pass

        elif first_screen.ch_tecido.active == True:
            try:
                reg = db.brief(first_screen.lb_tecido.text, first_screen.spin.text)
                for x in reg:
                    for z in x:
                        res.append(z)
                first_screen.lb_resumo.text = 'Nome : ' + res[1]
                first_screen.lb_cidade.text = 'Cidade: ' + res[2]
                first_screen.lb_nuped.text = 'Número do pedido: ' + str(res[3])
                first_screen.lb_data.text = 'Último pedido: ' + str(res[6]) + '/'+ str(res[7])+'/'+ str(res[8])
                first_screen.lb_valor.text = 'Valor: R$ ' + str(res[5])
            except:
                pass

        else:
            #first_screen.lb_resumo.text_size = [int(first_screen.lb_resumo.size[0]-50), None]
            first_screen.lb_resumo.text = 'Selecione segmento e cliente.'


        pass
    