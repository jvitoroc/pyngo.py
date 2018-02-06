from type import Types
from validators import validators

class Field:

    def __init__(self, constraints, name):
        self.name = name
        constraints['t'] = Types[constraints['t']]
        self.type = constraints['t']
        self.constraints = constraints

    def validate(self, value):
        for constraint, bullet in self.constraints.items():
            res = validators[constraint]((self.name, value), bullet)
            if(res[0]):
                raise Exception(res[1])
        if(self.type == Types.String):
            return ''.join(['"', value, '"'])
        else:
            return value

    def convert(self, value):
        if(self.type == Types.String):
            return value
        return self.type.value(value)