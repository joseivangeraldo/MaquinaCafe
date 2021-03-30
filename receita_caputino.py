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
