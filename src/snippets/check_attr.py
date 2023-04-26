# vim: ts=4 sw=4 sts=4 :
def chk_attr(attr_name, inst):
    inst_class = type(inst)

    if hasattr(inst, attr_name):
        if hasattr(inst_class, attr_name):
            instance_attr = getattr(inst, attr_name)
            class_attr = getattr(inst_class, attr_name)

            if instance_attr is not class_attr:
                print(f"{attr_name} is an inst attribute.")
            else:
                print(f"{attr_name} is a class attribute.")
        else:
            print(f"{attr_name} is an inst attribute.")
    else:
        print(f"{attr_name} is not an attribute of the inst or class.")

def list_attributes_and_check(inst):
    inst_class = type(inst)
    attrs = set(dir(inst)).union(dir(inst_class))

    for attr in attrs:
        if attr.startswith('__'): continue
        if callable(getattr(inst, attr)): continue
        chk_attr(attr, inst)

integer_instance = 123
list_attributes_and_check(integer_instance)

class C:
    cl_attr = "class attribute"
    def __new__(self):
        self.in_attr = "instance attribute"
    @staticmethod
    def st_method(): pass
    @classmethod
    def cl_method(cls): pass

c = C()
list_attributes_and_check(c)
list_attributes_and_check(C)

