def inicia_maquina(moeda,valor_pago,pedido):
    pedido = {'café':['médio'],
               'Caputino':['pequeno']
              }
    if moeda == True and valor_pago == 10 :
        print('Tudo OK')
        print(receita_caputino(20,True))
        
    else:
        print('Houve algum erro')
inicia_maquina(True,10,'café')
