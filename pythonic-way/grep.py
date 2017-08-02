#!/usr/bin/python
# Grep do unix implementado em python
# Gabriel Fernandes


from __future__ import print_function

import re
from sys import argv


# grep baseado em corotina
def grep(padrao):
    num_linhas = 0
    exp_reg = re.compile(padrao)
    while 1:
        linha = yield
        num_linhas += 1
        if exp_reg.findall(linha):
            yield str(num_linhas) + ':' + linha
        else:
            yield


def main():
    if len(argv) < 3:
        print('Uso: python grep.py <padrao> <arquivo>')
    else:
        corotina = grep(argv[1])
        for linha in open(argv[2]):
            next(corotina)
            resp = corotina.send(linha)
            if resp:
                print(resp, end='')


if __name__ == '__main__':
    main()
