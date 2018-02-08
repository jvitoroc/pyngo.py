"""
Constraints validators: a validator returns True if it's violated,
otherwise return the target value
"""
"""
target[0] == field name
target[0] == field value
"""
def typee(target, bullet):
    try:
        v = bullet.value(target[1])
        return (False, v)
    except TypeError:
        if (type(target[1]) == bullet.value):
            return (False, v)
        else:
            raise TypeError()
    except:
        return (True, "Type does not match: \"{}\" must be of type {}".format(target[0], bullet))

def maxl(target, bullet):
    if(len(target[1]) > bullet):
        return (True, "Field \"{}\" violated the constraint maxl".format(target[0]))
    return (False, target)

def minl(target, bullet):
    if(len(target[1]) < bullet):
        return (True, "Field \"{}\" violated the constraint minl".format(target[0]))
    return (False, target)


#Export validators
validators = {
    "maxl": maxl,
    "minl": minl,
    "t": typee
}