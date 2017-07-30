#!/usr/bin/python3
# simples execucao assincrona usando python generators
# Gabriel Fernandes


# gera a quantidade desejada de numeros pares
# tam :: tamanho da sequencia desejada
def pares(tam):
    n = 0
    while n < tam:
        yield 2*n
        n += 1


# gera a quantidade desejada de numeros impares
# tam :: tamanho da sequencia desejada
def impares(tam):
    n = 0
    while n < tam:
        yield 2*n + 1
        n += 1


# gera a quantidade desejada de numeros pares e impares
# tam :: tamanho da sequencia desejada
def pares_impares(tam):
    gen_pares = pares(tam//2 + tam%2)
    gen_impares = impares(tam//2)
    for par in gen_pares:
        yield par
        yield next(gen_impares)


def main():
    print('Gerando somente pares:')
    for n in pares(10):
        print(n, end=' ')
    print('\n')

    print('Gerando somente impares:')
    for n in impares(10):
        print(n, end=' ')
    print('\n')

    print('Gerando pares e impares ao "mesmo tempo":')
    for n in pares_impares(10):
        print(n, end=' ')
    print()


if __name__ == '__main__':
    main()
