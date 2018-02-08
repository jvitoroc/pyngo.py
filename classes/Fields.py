from type import Types
import pyparsing as pp
import re
from classes.Field import Field

def createParser(order, fields):
    parser = pp.Suppress(pp.LineStart())

    for field in order:
        type = fields[field].type
        if(type == Types.String):
            parser += pp.QuotedString('"').setResultsName(field)+pp.Suppress(pp.Literal(" "))
        elif(type == Types.Boolean):
            parser += pp.Regex("(True|False)").setResultsName(field)+pp.Suppress(pp.Literal(" "))
        elif(type == Types.Integer):
            parser += pp.Regex("\d+").setResultsName(field)+pp.Suppress(pp.Literal(" "))
    return parser + pp.Suppress(pp.LineEnd())

def createParser(order, fields):
    regex

class Fields:

    def __init__(self, fields):
        self.fields = {}
        self.order = []
        for field in fields:
            name = field['n']
            self.fields[name] = Field(field['c'], name)
            self.order.append(field['n'])
        self.parser = createParser(self.order, self.fields)

    def __getitem__(self, field):
        return self.fields[field]

    def validate(self, values):
        for field, value in values.items():
            values[field] = self.fields[field].validate(value)
        return values
