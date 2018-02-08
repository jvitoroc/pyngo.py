import pyparsing as pp
from type import Types

def createParser(order, fields):
    parser = pp.Suppress(pp.LineStart())

    for field in order:
        type = fields[field].type
        if(type == Types.String):
            parser += pp.QuotedString('"', multiline=True, escChar="\"").setResultsName(field)+pp.Suppress(pp.Literal(" "))
        elif(type == Types.Boolean):
            parser += pp.Regex("(True|False)").setResultsName(field)+pp.Suppress(pp.Literal(" "))
        elif(type == Types.Integer):
            parser += pp.Regex("\d+").setResultsName(field)+pp.Suppress(pp.Literal(" "))
    return parser + pp.Suppress(pp.White(exact=1)+pp.LineEnd())

class CollectionIO:

    def __init__(self, path, order, fields):
        self.path = '{}/data/{}.col'.format(path[0], path[1])
        self.file = open(self.path, 'ab+')
        self.order = order
        self.parser = createParser(self.order, fields)

    def createReader(self):
        self.file.seek(0)
        for record in self.file:
            print(record.decode('unicode-escape'))
            yield self.parser.parseString(record.decode('unicode-escape'))

    def write(self, values):
        insertion = []
        for field in self.order:
            insertion.append(str(values[field]))
        self.file.write(" ".join(insertion).encode('unicode-escape'))
        self.file.write(b"\n")

    # def __iter__(self):
    #     return self
    #
    # # Also know as read
    # def next(self):
    #     self.file.seek(0)
    #     for record in self.file:
    #         return record