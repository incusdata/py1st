# Example function to find members in an objects.

import types

def is_static_method(klass, attr):
    for cls in klass.__mro__:
        if attr in cls.__dict__:
            return isinstance(cls.__dict__[attr], staticmethod)
    return False

def is_class_method(klass, attr):
    for cls in klass.__mro__:
        if attr in cls.__dict__:
            ga = getattr(cls, attr)
            return isinstance(ga, classmethod) or \
                isinstance(ga, types.BuiltinFunctionType)
    return False

def members(arg):
    if isinstance(arg, type):
        cls, obj = arg, arg()
    else:
        cls, obj = arg.__class__, arg
    for name in dir(cls):
        atr = getattr(cls, name)
        if name.startswith('__'): continue
        if callable(atr):
            if is_class_method(cls, name):
                print(f"class method : {name} {atr}")
            elif is_static_method(cls, name):
                print(f"static method: {name} {atr}")
            else:
                print(f"inst. method : {name} {atr}")
        else:
            if "attribute" in str(atr):
                print(f"inst. attrib.: {name} {atr}")
            else:
                print(f"class attrib.: {name} {atr}")
    for name in dir(obj):
        atr = getattr(obj, name)
        if name.startswith('__'): continue
        if callable(atr):
            if is_class_method(cls, name):
                print(f"class method : {name} {atr}")
            elif is_static_method(cls, name):
                print(f"static method: {name} {atr}")
            else:
                print(f"inst. method : {name} {atr}")
        else:
            if "attribute" in str(atr):
                print(f"inst. attrib.: {name} {atr}")
            else:
                print(f"class attrib.: {name} {atr}")

class CA:
    def __new__(self):
        self.in_attr = "instance"
    
    @classmethod
    def cl_method(): pass
    
    @staticmethod
    def st_method(): pass
    cl_attr = 123

    def in_method(): pass

print("━" * 80)
members(CA)
print("-" * 80)
members(CA())
print("━" * 80)
members(int())
