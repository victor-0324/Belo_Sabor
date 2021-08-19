# Belo_Sabor
Controle de vendas 

## Vamos  forma Uma base de dados dos cliente de uma loja de comidas 

###  vamos importa as bibliotecas que serao necessarias 
-     from datetime import datetime
-     import csv 
-     from tkinter import *
-     import pandas as pd 
-     import time

## Agora vamos pega a hora exata que esta sendo executado o codigo
-     now = datetime.now().strftime("%d/%m/%Y")
-     print(f"Hora a Tual Do Cadastro: {now}\n") 

## E ai entao começamos o nosso laço de reptição while para da inicio
-   while True:
-     print('<<<<Base_De_Dados do Belo Sabor>>>>\n')
-     data1 = input('informe a data do pedido ou digite 1 para atualizar com a data de hoje:\n> ')
-     if data1 == '1':
-        data = now 
-        print('ok, data atual selecionada') 

