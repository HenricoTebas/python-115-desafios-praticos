'''co = float(input("Compreimento do cateto oposto: "))
ca = float(input("Compreimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}' .format(hi))'''

from math import hypot
co = float(input("Compreimento do cateto oposto: "))
ca = float(input("Compreimento do cateto adjacente: "))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}' .format(hi))