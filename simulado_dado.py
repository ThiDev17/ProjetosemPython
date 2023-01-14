#simulador de dados
# simula um valor de um dado gerando de 1 até 6

import random
import PySimpleGUI as sg
class simuladador_dado:
    def __init__(self):
        self.valor_menor = 1 
        self.valor_maior = 6
        self.mensagem = "voce gostaria de um novo valor para o dado?"
    #layout
        self.layout = [
        [sg.Text("joga o dado")],
        [sg.Text("sim"), sg.Button("não")]
    ]
    #criar janela
        self.janela = sg.Window("Simulador de dado",Layout=self.layout)
    #ler os valores da tela
        self.event, self.valores = self.janela.Read()
    #fazer alguma coisa com esses valores 
    while True:
       try:
           if self.eventos == "sim" or self.eventos == "s":
            self.gerarvalor()
       elif self.eventos == "não" or self.resposta == "n":
          print('agradeço a sua participação')
        else:
            print('favor digita sim ou não')

      
       except:
             print("ocorreu erro ao recebe sua resposta")
             def geravalor(self):
              print(random.randint(self.valor_menor,self.valor_maior))
    simulado = simuladador_dado()
    simulado.start()
      


 
    


         