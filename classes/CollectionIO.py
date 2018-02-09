import sPickle

class CollectionIO:

    def __init__(self, path, order, fields):
        self.path = '{}/data/{}.col'.format(path[0], path[1])
        self.file = open(self.path, 'ab+')
        self.fieldsLength = len(order)


    def createReader(self):
        i = 0
        record = {}
        for r in sPickle.s_load(self.file):
            record[r[0]] = r[1]
            i += 1
            if(i == self.fieldsLength):
                yield record
                record = {}
                i = 0

    def write(self, record):
        sPickle.s_dump(record.items(), self.file)

    # def __iter__(self):
    #     return self
    #
    # # Also know as read
    # def next(self):
    #     self.file.seek(0)
    #     for record in self.file:
    #         return record