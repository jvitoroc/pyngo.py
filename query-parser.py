import pyparsing as pp

cmd = pp.Or([pp.Literal('insert'), pp.Literal('get')]).setResultsName('cmd')
collection = pp.Word(pp.alphas)('collection').setResultsName('collection')
white = pp.Suppress(pp.ZeroOrMore(pp.White()))

operator = pp.Regex(">=|<=|!=|>|<|=").setName("operator")
number = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")
boolean = pp.Or([pp.Literal("False"), pp.Literal("True")])
identifier = pp.Word(pp.alphas, pp.alphanums + "_")
comparison_term = identifier | number | boolean
condition = pp.Group(comparison_term + operator + comparison_term)

expr = pp.operatorPrecedence(condition,[
                            ('and', 2, pp.opAssoc.LEFT, ),
                            ("or", 2, pp.opAssoc.LEFT, ),
                            ])

print(expr.parseString("x > True and x < 8 or x = 4"))
