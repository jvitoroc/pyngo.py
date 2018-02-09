
class Record:

    def __init__(self, values, fields):
        self.values = values
        self.fields = fields

    def extract(self):
        return self.fields.convert(self.values)