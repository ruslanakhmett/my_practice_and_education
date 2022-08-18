#ПОЛИМОРФИЗМ И АБСТРАКТНЫЕ КЛАССЫ
#абстрактный класс - это класс, от которого можно производить наследование,
#но его самого нельзя использоваться что бы что-то инициализировать
# ABC - abstract base class

from abc import ABC, abstractmethod


class Shipping(ABC):
    @abstractmethod
    def shipping(self, transport):
        pass


class Electrical_Appliance(ABC): #абстрактный класс
    def __init__(self):
        super().__init__()

    @abstractmethod
    def electricity_potrebleine():
        pass



class Heater(Electrical_Appliance, Shipping):
    def __init__(self, heating):
        self.heating = heating

    def electricity_potrebleine(self):
        return 1500 * self.heating

    def shipping(self, transport):
        self.transport = transport
        return transport



class Cooler():
    def __init__(self, cooling):
        self.cooling = cooling
    
    def electricity_potrebleine(self):
        return 300 * self.cooling



h = Heater(50)
print(h.heating, h.electricity_potrebleine(), h.shipping("Cargo ship"))

c = Cooler(20)
print(c.cooling, c.electricity_potrebleine())