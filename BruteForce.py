# coding: utf-8

import sys

def isCostas(a):
    for d in range(1, len(a) - 1):
        elements = set()
        for d_i, d_j in zip(a, a[d:]):
            if (d_i - d_j) in elements:
                return False
            elements.add(d_i - d_j)
    return True

def RecursiveAllCostas(n, lista=tuple()):
    if len(lista) == n and isCostas(lista):
        yield lista
    for value in range(n):
        if value not in lista:
            new = lista + (value, )
            if isCostas(new):
                yield from RecursiveAllCostas(n, new)

if __name__ == '__main__':
    numero = 0
    for i in RecursiveAllCostas(int(sys.argv[1])):
        numero += 1
    print(numero)
