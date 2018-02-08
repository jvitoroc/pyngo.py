import json
from classes.Collection import Collection

class Definition:

    def __init__(self, path):
        self.file = open(path+'/def.json', 'r+')
        self.collections = {}
        buffer = json.loads(self.file.read())
        for name, fields in buffer.items():
            self.collections[name] = Collection(fields, name, path)

    """
    Create a collection
    returns a Collection instance
    """

    def __enter__(self):
        return self.collections

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        for (_, coll) in self.collections.items():
            del coll

    def createCollection(self, name, constraints):
        pass

    def deleteCollection(self, name):
        pass

    def push(self):
        pass