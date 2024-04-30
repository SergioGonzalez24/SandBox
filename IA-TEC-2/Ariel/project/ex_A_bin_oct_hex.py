# Author: A01745446 Sergio Gonzalez

from delta import Compiler, Phase

source = '#o431870'

c = Compiler('program')
c.realize(source)
print()
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
# print(c.wat_code)
print()
print(c.result)