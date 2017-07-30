#!/usr/bin/python3
# simples execucao assincrona usando python iterators
# Gabriel Fernandes


# iterator que gera numeros pares
# tam :: tamanho da sequencia desejada
class Pares:
    def __init__(self, tam):
        self.tam = tam

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.tam:
            total = 2*self.n
            self.n += 1
            return total
        else:
            raise StopIteration


# iterator que gera numeros impares
# tam :: tamanho da sequencia desejada
class Impares:
    def __init__(self, tam):
        self.tam = tam

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.tam:
            total = 2*self.n + 1
            self.n += 1
            return total
        else:
            raise StopIteration


# iterator que gera numeros pares e impares
# tam :: tamanho da sequencia desejada
class Pares_Impares:
    def __init__(self, tam):
        self.tam = tam
        self.iter_pares = Pares(tam//2 + tam%2).__iter__()
        self.iter_impares = Impares(tam//2).__iter__()

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.tam:
            if self.n%2 == 0:
                total = next(self.iter_pares)
            else:
                total = next(self.iter_impares)
            self.n += 1
            return total
        else:
            raise StopIteration


def main():
    print('Gerando somente pares:')
    for n in Pares(10):
        print(n, end=' ')
    print('\n')

    print('Gerando somente impares:')
    for n in Impares(10):
        print(n, end=' ')
    print('\n')

    print('Gerando pares e impares ao "mesmo tempo":')
    for n in Pares_Impares(10):
        print(n, end=' ')
    print()


if __name__ == '__main__':
    main()
