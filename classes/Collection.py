from classes.Fields import Fields

class Collection:

    def __init__(self, fields, name, path):
        self.name = name
        self.path = path
        self.fields = Fields(fields)
        self.file = open('{}/data/{}.col'.format(path, name), 'a+', encoding='utf-8')

    def insert(self, values):
        insertion = []
        res = self.fields.validate(values)
        self.file.seek(2)
        if(res is not False):
            for field in self.fields.order:
                insertion.append(str(res[field]))
            insertion.append("\n")
            self.file.write(" ".join(insertion))
        pass

    def read(self, filter=None):
        res = []
        fields = self.fields
        self.file.seek(0)
        for record in self.file:
            data = self.fields.parser.parseString(record)
            rd = {}
            for field in self.fields.order:
                rd[field] = fields[field].convert(data[field])
            res.append(rd)
        return res
        pass

    # of course I will update this function soon
    def delete(self, filter=None):
        with open('{}/data/{}.col'.format(self.path, self.name), 'w') as f:
            f.seek(0)
            f.write('')
        pass