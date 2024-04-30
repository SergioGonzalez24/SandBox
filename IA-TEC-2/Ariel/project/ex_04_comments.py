from delta import Compiler, Phase


source = '''
/*
 This is a comment.
 */
7
+ // This is a comment
5
/* This is a block comment */
'''

c = Compiler('program')
c.realize(source)
print()
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)