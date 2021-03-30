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

