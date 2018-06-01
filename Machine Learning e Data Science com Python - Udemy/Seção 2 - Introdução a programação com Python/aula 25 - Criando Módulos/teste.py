# -*- coding: utf-8 -*-

from my_math import area_quad
from my_math import area_ret
from my_math import peri_quad

from my_convert import list_to_tuple  
#função de converssão de lista para tupla

print(area_quad(5))
print(area_ret(5, 10))
print(peri_quad(10))


#criando uma lista
lista = [1,2,3,4]
print(lista)  

tupla = list_to_tuple(lista)
print(tupla)