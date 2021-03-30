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
