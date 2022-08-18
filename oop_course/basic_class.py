class Car:
    PURCHASE_TYPES = ("LEASE", "CASH") # методы и атрибуты на уровне класса

    __sales_list = None #  скрытый список внутри класса

    @staticmethod
    def get_sales_list(): # определяем статический метод
        if  Car.__sales_list == None:
            Car.__sales_list = []
        return Car.__sales_list

    @classmethod
    def get_purchase_types(cls): # метод для использования внутри класса
        return cls.PURCHASE_TYPES


    def __init__(self, maker, model, color, price, purchase_type):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price
        self.__secret_cog = "Tshhh" # приватный атрибут
        if (not purchase_type in Car.PURCHASE_TYPES):
            raise ValueError(f"{purchase_type} is not a valid purchase type")
        else:
            self.purchase_type = purchase_type


    def get_price(self):
        if hasattr(self, "_discount"):  # проверяет есть ли такой атрибут у экземпляра
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount  # _discount - является внутриклассовым, не использовать за пределами(модификатор доступа)

class Boat:
    def __init__(self, name):
        self.name = name



car1 = Car("BMW", "i8", "white", 50000, "CASH")
car2 = Car("Mercedes", "C-class", "black", 28500, "LEASE")

#sales_this_month = Car.get_sales_list()
#sales_this_month.append(car1)
#sales_this_month.append(car2)

#print(sales_this_month)


#print("Purchase types: ", Car.get_purchase_types())

#print(car1.purchase_type)
#print(car2.purchase_type)


#boat1 = Boat("Titanik")

#print(isinstance(car1, object))
#print(isinstance(car1, Car))

#print(type(car1))
#print(type(boat1))
#print(type(car2) == type(car1))

#print(car1.get_price())
#car2.set_discount(0.25)
#print(car2.get_price())

#print(car2.__secret_cog)  # ошибка
#print(car2._Car__secret_cog)  #а так можно вызвать