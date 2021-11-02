from lark import Lark
text = '{"key": ["item0", "item1", 3.14]}'

jso_parser = Lark(r"""
    value: dict
         | list
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')
print(jso_parser.parse(text))
print(jso_parser.parse(text).pretty())
#
# json_parser = Lark(r"""
#     ?value: dict
#           | list
#           | string
#           | SIGNED_NUMBER      -> number
#           | "true"             -> true
#           | "false"            -> false
#           | "null"             -> null
#
#     list : "[" [value ("," value)*] "]"
#
#     dict : "{" [pair ("," pair)*] "}"
#     pair : string ":" value
#
#     string : ESCAPED_STRING
#
#     %import common.ESCAPED_STRING
#     %import common.SIGNED_NUMBER
#     %import common.WS
#     %ignore WS
#
#     """, start='value')
#
# tree = json_parser.parse(text)
# print(tree.pretty())
#
# from lark import Transformer
# class MyTransformer(Transformer):
#     def list(self, items):
#         return list(items)
#     def pair(self, key_value):
#         k, v = key_value
#         return k, v
#     def dict(self, items):
#         return dict(items)
#
# class TreeToJson(Transformer):
#     def string(self, s):
#         (s,) = s
#         return s[1:-1]
#     def number(self, n):
#         (n,) = n
#         return float(n)
#
#     list = list
#     pair = tuple
#     dict = dict
#
#     null = lambda self, _: None
#     true = lambda self, _: True
#     false = lambda self, _: False
#
# print(MyTransformer().transform(tree))
# print(TreeToJson().transform(tree))
#
# class T (Transformer):      #Use transformer to parse integer tokens
#     def INT(self, tok):
#         return tok.update(value=int(tok))
#
# parser = Lark("""
# start: INT*
# %import common.INT
# %ignore " "
# """, parser="lalr", transformer=T())
#
# print(parser.parse('3 14 159'))
#
# comments = []               # collect all comments with lexer_callbacks
#
# par = Lark("""
#     start: INT*
#
#     COMMENT: /#.*/
#
#     %import common (INT, WS)
#     %ignore COMMENT
#     %ignore WS
# """, parser="lalr", lexer_callbacks={'COMMENT': comments.append})
#
# par.parse("""
# 1 2 3  # hello
# # world
# 4 5 6
# """)
#
# print(comments)

# grammar = """
#     sentence: noun verb noun        -> simple
#             | noun verb "like" noun -> comparative
#
#     noun: adj? NOUN
#     verb: VERB
#     adj: ADJ
#
#     NOUN: "flies" | "bananas" | "fruit"
#     VERB: "like" | "flies"
#     ADJ: "fruit"
#
#     %import common.WS
#     %ignore WS
# """
# parser = Lark(grammar, start='sentence', ambiguity='explicit')
# sentence = 'fruit flies like bananas'
# print(parser.parse(sentence).pretty())
#
#
# turtle_text = """
# c red yellow
# fill { repeat 36 {
#     f200 l170
# }}
# """
#
# grammar_1 = """
#     start: instruction+
#     instruction: MOVEMENT NUMBER                -> movement
#                 | "c" COLOR [COLOR]             -> change_color
#                 | "fill" code_block             -> fill
#                 | "repeat" NUMBER code_block    -> repeat
#     code_block: "{" instruction+ "}"
#
#     MOVEMENT: "f"|"b"|"l"|"r"
#     COLOR: LETTER+
#
#     %import common.LETTER
#     %import common.INT -> NUMBER
#     %import common.WS
#     %ignore WS
# """
# parser_1 = Lark(grammar_1)
# print(parser_1.parse(turtle_text).pretty())