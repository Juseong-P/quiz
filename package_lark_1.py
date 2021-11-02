from lark import Lark, Transformer

grammar = """
?start: addexpr
    | subexpr

addexpr: NUMBER "+" NUMBER
subexpr: NUMBER "-" NUMBER
%import common.NUMBER
%ignore " "
"""
p = Lark(grammar)

print(p.parse("1+1"))
print(p.parse("2-1"))
print(p.parse("3 - 2"))

print(p.parse("1+1").pretty())
print(p.parse("2-1").pretty())
print(p.parse("3 - 2").pretty())

class CalcTransformer(Transformer):
    def addexpr(self, args):
        return int(args[0]) + int(args[1])
    def subexpr(self, args):
        return int(args[0]) - int(args[1])

parser = Lark(grammar, parser='lalr', transformer=CalcTransformer())

def main():
    print(parser.parse("1+1"))
    print(parser.parse("2-1"))
    print(parser.parse("3 - 2"))

if __name__ == '__main__':
    main()
