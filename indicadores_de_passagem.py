meu_cartao = int(input('Digite o número do seu cartão de crédito: '))

cartao_lido = 1
cartao_encontrado = False

while cartao_lido != 0 and not cartao_encontrado:
    cartao_lido = int(input('Digite o número do próximo cartão de crédito'))
    if cartao_lido == meu_cartao:
        cartao_encontrado = True


if cartao_encontrado:
    print('EBA!! meu cartão está lá!')
else:
    print('Xi, meu cartão não está la!')


