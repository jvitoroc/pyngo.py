from classes.Field import Field

class Fields:

    def __init__(self, fields):
        self.fields = {}
        for field in fields:
            name = field['n']
            self.fields[name] = Field(field['c'], name)

    def _iter_(self, field):
        return self.fields.values()

    def validate(self, values):
        for field, value in values.items():
            self.fields[field].validate(value)
        return values

    def convert(self, values):
        converted = {}
        for f in self.fields:
            converted[f] = self.fields[f].convert(values[f])
        return converted