temperatura = 102

if temperatura:
	aguaFerve = True
	evaporacao = 'muito rápida'

print(aguaFerve)
print(evaporacao)
print('='*20)

tempoDeJogo = int(input('Quanto tempo temos já jogado ? '))


if tempoDeJogo <= 90:
	print('Ainda tem jogo pela frente')
	print('Que bom, quero assistir')
else:
	print('Está acabando o jogo')
	print('Apita logo, Juiz!!!')


