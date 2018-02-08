from classes.Field import Field

class Fields:

    def __init__(self, fields):
        self.fields = {}
        for field in fields:
            name = field['n']
            self.fields[name] = Field(field['c'], name)

    def __getitem__(self, field):
        return self.fields[field]

    def validate(self, values):
        for field, value in values.items():
            values[field] = self.fields[field].validate(value)
        return values
