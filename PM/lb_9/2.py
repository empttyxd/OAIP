class AutoRegister(type):
    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        if bases:
            base_class = bases[0]
            if hasattr(base_class, 'registry'):
                base_class.registry.append(obj)
        return obj


class BaseModel(metaclass=AutoRegister):
    registry = []


class User(BaseModel):
    pass


class Product(BaseModel):
    pass


print(BaseModel.registry)
