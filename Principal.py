confirmapedido = True #@param {type:"boolean"}
valorpago =  25#@param {type:"integer"}
total = []
def receita_cafe(dinheiro,confirma_pedido):
    preco = 10
    if dinheiro == preco and confirma_pedido:
        operacao = True
        while operacao :
            agua = 100
            acucar = 20
            cafe = 20   
            aeração = True
            dosar = [30,50,100]
            for i in dosar:
                if dosar[0]== 30:
                    operacao = False
                    return 'Obrigado seu pedido foi realizado.'
                else:
                  return 'Desculpe houve algum erro'
print(receita_cafe(10,confirmapedido))


def receita_caputino(dinheiro,confirma_pedido):
    preco = 20
    if dinheiro == preco and confirma_pedido:
        operacao = True
        while operacao :
            agua = 100
            acucar = 20
            cafe = 20   
            aeração = True
            dosar = [30,50,100]
            for i in dosar:
                if dosar[0]== 30:
                    for j in dosar:
                        operacao = False
                        return agua 
print(receita_caputino(20,True))

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

 
botao_devolve_moedas = False
def dinheiro(pes_moedas):
    total_moedas = 0
    valor = 0
    sensor_balanca = True
    sensor_moedas = True
    botao_pedido = False
 
    if not sensor_moedas :
        print('coloque moedas')
    else:
      if sensor_moedas:
        if pes_moedas == 5:
          valor = valor + 5
        elif pes_moedas == 10:
          valor = valor + 10
        elif pes_moedas == 25:
          valor = valor + 25
        elif pes_moedas == 50:
          valor = valor + 50
        elif pes_moedas == 100:
          valor = valor + 100
    return valor
peso_moedas = {'cinco_centavos':5,
               'dez_centavos':10,
               'vinte_cinco_centavos':25,
               'cinquenta_centavos':50,
               'um_real':100,
               'zero_centavos':0,
               }
sensor_moedas = True
if sensor_moedas and not botao_devolve_moedas:
  valor = dinheiro(peso_moedas['cinco_centavos'])
  total.append(valor) 
  print(sum(total))
else:
  if sensor_moedas and botao_devolve_moedas:
    print('Houve algum erro contate fabricante!')
  elif botao_devolve_moedas:
    del total[0:]
    print(total)
