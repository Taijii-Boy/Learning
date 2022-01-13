# class Geom:
#     pass

# class Line(Geom):
#     pass


# l = Line()
# g = Geom()
# # print(Line.__name__)
# print(issubclass(Line, Geom))
# print(issubclass(Geom, Line))
# print(isinstance(l, Line))
# print(isinstance(l, Geom))
# print(isinstance(Geom, object))


class Vector(list):
    # pass
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)