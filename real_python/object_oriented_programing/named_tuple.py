# named_tuple.py

from operator import itemgetter

def named_tuple_factory(type_name, *fields):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()
    
        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} expected exactly {num_fields} "
                    f"argument, got {len(args)}"
                )
            cls.__name__ = type_name
            for index, field in enumerate(fields):
                setattr(cls, field, property(itemgetter(index)))
            return super().__new__(cls, args)

        def __repr__(self):
            return f"""{type_name} ({", ".join(repr(arg) for arg in self)})"""
    
    return NamedTuple

Point = named_tuple_factory("Point", "x", "y")
point = Point(21, 42)
print(point.x)
print(point.y)
print(point[0])
print(point[1])
