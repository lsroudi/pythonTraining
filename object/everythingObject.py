x = 1

def idObject(o):
    return id(o)

def typeObject(o):
    return type(o)


print(idObject(x))   # object has id
print(typeObject(x)) # the class of x or ourType
