from pickle import dumps, loads, HIGHEST_PROTOCOL


class StreamingPickle:

    def __init__(self, path, delimiter=b'\n * - * \n'):
        self.file = open(path, 'ab+')
        if(delimiter[0] == 10):
            self.rDelimiter = delimiter[1:]
            self.delimiter = delimiter
        else:
            self.delimiter = b'\n' + delimiter[1:]
            self.rDelimiter = delimiter

    def write(self, object):
        pickled = dumps(object, protocol=HIGHEST_PROTOCOL)
        self.file.write(pickled)
        self.file.write(self.delimiter)

    def read(self):
        self.file.seek(0)
        frags = []
        for line in self.file:
            if line == self.rDelimiter:
                pickled = b''.join(frags)
                res = loads(pickled)
                frags = []
                yield res
                continue
            frags.append(line)
