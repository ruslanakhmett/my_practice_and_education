class Vehicle:   #родительский класс (транспорт)
    def __init__(self, maker, model, color, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price

class Car(Vehicle):
    def __init__(self, maker, model, color, price, seats):
        super().__init__(maker, model, color, price) # таким образом мы наследуем у рдительского класса нужные нам атрибуты
        self.seats = seats



class IndustrialVehicle(Vehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price)
        self.lifting_weight = lifting_weight


class Forklift(IndustrialVehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price, lifting_weight)


class Crane(IndustrialVehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price, lifting_weight)



car1 = Car("Opel", "Mokka", "Black", 20000, 5)
forklift1 = Forklift("Honda", "FK1", "Orange", 15000, 5)
crane1 = Crane("Caterpillar", "fr4", "Yellow", 65000, 55)

print(car1.maker, car1.model, car1.color, car1.price, car1.seats)
print(forklift1.maker, forklift1.model, forklift1.color, forklift1.price, forklift1.lifting_weight)
print(crane1.maker, crane1.model, crane1.color, crane1.price, crane1.lifting_weight)