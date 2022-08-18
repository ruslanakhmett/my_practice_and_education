#множественное наследование - наследование от к примеру двух родителей одним потомком


class Parent1:
    def __init__(self):
        super().__init__()
        self.smart = "smart"
        self.hair_colour = "light"

class Parent2:
    def __init__(self):
        super().__init__()
        self.pretty = "pretty"
        self.hair_colour = "dark"


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()

    def traits(self):
        print(self.pretty)
        print(self.smart)
        print(self.hair_colour)

# при совпадении атрибутов, питон берет первый по порядку, сперва ищет в ребенке, потом в родителях по порядку сверху вниз

child = Child()
child.traits()
