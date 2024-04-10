from delta import Compiler, Phase


source = '123'

c = Compiler('program')
c.realize(source, Phase.SEMANTIC_ANALYSIS)
# print(c.parse_tree_str)
print(c.wat_code)
print(c.result)
