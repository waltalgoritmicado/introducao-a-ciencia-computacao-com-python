import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):    
    if delta(a, b, c) == 0:
        raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        print('A única raiz é:', raiz1)

    else:
        if delta(a, b, c) < 0:
            print('Esta equação não possui raízes reais')
        else:
            raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a) 
            raiz2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
            print('A primeira raíz é: ', raiz1)
            print('A segunda raíz é: ', raiz2)

main()

