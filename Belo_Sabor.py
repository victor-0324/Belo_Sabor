from datetime import datetime
import csv 
from tkinter import *
import pandas as pd 
import time

now = datetime.now().strftime("%d/%m/%Y")
print(f"Hora a Tual Do Cadastro: {now}\n") 

while True:
    print('<<<<Base_De_Dados do Belo Sabor>>>>\n')
    data1 = input('informe a data do pedido ou digite 1 para atualizar com a data de hoje:\n> ')
    if data1 == '1':
        data = now 
        print('ok, data atual selecionada')
       
    elif data1 != '1':
        data = data1
    else:
        print('digite 1 ou informe a data do pedido!')
        
    cliente = input('Qual o nome do cliente:\n> ')  
    telefone = input(f'Qual o numero de telefone de {cliente}:\n> ')
    produto = input('Qual e o pedido do cliente :\n> ')

    tempo_micro_ondas = input('Quanto minutos foi usado no micro ondas para o cliente:\n> ')
    total_pedido = input(f'Quanto foi o total do pedido de {cliente}:\n> ')
    #pergunta = input('deseja manda uma mensagem hoje se sim digite 1 se não digite 2 ?\n> ')
    continua = input('Deseja anexa mais um cliente? SIM digite 1, NAO digite 2:\n')

    if continua == '1':
        dados_resposta = [cliente,telefone,produto,tempo_micro_ondas,total_pedido,data]
        dados_responde = ['cliente','tel','pedidos','minutos_micro_ondas','total_compras','data']
        with open("Belo_Sabor.csv", "a", encoding='utf-8') as ficheiro:
            writer =  csv.writer(ficheiro)   
            for intems in dados_responde,dados_resposta:              
                writer.writerow(intems)  
        time.sleep(1)
        print('Ok arquivo atualizado\n')
        print('novo arquivo>\n')
        continue

    elif continua == '2':
        dados_resposta = [cliente,telefone,produto,tempo_micro_ondas,total_pedido,data]
        dados_responde = ['cliente','tel','pedidos','minutos_micro_ondas','total_compras','data']
        with open("Belo_Sabor.csv", "a", encoding='utf-8') as ficheiro:
            writer =  csv.writer(ficheiro)   
            for intems in dados_responde,dados_resposta:              
                writer.writerow(intems)  
        time.sleep(1)
        print('Ok arquivo atualizado\n')
        break 
    else:
        print(' Erro! Digite 1 ou 2')
        
    '''dados_resposta = [cliente,telefone,produto,tempo_micro_ondas,total_pedido,data]
    dados_responde = ['cliente','tel','pedidos','minutos_micro_ondas','total_compras','data']

    with open("Belo_Sabor.csv", "w", encoding='utf-8') as ficheiro:
        writer =  csv.writer(ficheiro)   
        for intems in dados_responde,dados_resposta:              
            writer.writerow(intems)  
    time.sleep(1)'''

        
    '''if pergunta == '1' :
        mensagem = input('Cole a mensagem do cliente:')
        recebidos = [cliente,telefone,mensagem]
        colunas = ['cliente','telefone','Mensagems']

        with open("envir.csv", "w", encoding='utf-8') as f:
            writer =  csv.writer(f)   
            for i in colunas,recebidos:              
                writer.writerow(i)  

    elif pergunta == '2':
        print('Ok.')    
    else:
        print('1 ou 2 deu erro')'''

    
    

