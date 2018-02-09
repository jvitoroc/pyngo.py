from classes.StreamingPickle import StreamingPickle

class CollectionIO:

    def __init__(self, path, order, fields):
        self.path = '{}/data/{}.col'.format(path[0], path[1])
        self.streamFile = StreamingPickle(self.path)
        self.fieldsLength = len(order)

    def createReader(self):
        for r in self.streamFile.read():
            yield r

    def write(self, record):
        self.streamFile.write(record)

    # def __iter__(self):
    #     return self
    #
    # # Also know as read
    # def next(self):
    #     self.file.seek(0)
    #     for record in self.file:
    #         return record