from classes.Fields import Fields
from classes.CollectionIO import CollectionIO
from classes.Record import Record

class Collection:

    def __init__(self, fields, name, path):
        self.name = name
        self.path = '{}/data/{}.col'.format(path, name)
        self.fields = Fields(fields)
        order = []
        for field in fields:
            order.append(field['n'])
        self.StorageIO = CollectionIO((path, name), order, self.fields)

    def insert(self, values):
        res = self.fields.validate(values)
        if(res is not False):
            self.StorageIO.write(values)
        pass

    def read(self, filter=None):
        reader = self.StorageIO.createReader()
        res = []
        for record in reader:
            res.append(Record(record, self.fields).extract())
        return res

    #of course I will update this function soon
    def delete(self, filter=None):
        pass
        # with open('{}/data/{}.col'.format(self.path, self.name), 'w') as f:
        #     f.seek(0)
        #     f.write('')
        # pass