class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''


class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self__numberCylinders = 1
        
        
    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self__numberDrives = 2
        
    def getNumberDrives(self):
        return self.__numberDrives
        
    def setNumberDrives(self, value):
        self.__numberCylinders = value

        
class CarRental(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_stock(self):
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range (8) :
            self.diesel_cars.append(DieselCar())
        for i in range (4) :
            self.hybrid_cars.append(HybridCar())

    def stock_count(self):
        print 'petrol cars in stock ' + str(len(self.petrol_cars))
        print 'electric cars in stock ' + str(len(self.electric_cars))
        print 'diesel cars in stock ' + str(len(self.diesel_cars))
        print 'hybrid cars in stock ' + str(len(self.hybrid_cars))
        
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    def process_rental(self):
        answer = raw_input('would you like to rent a car? y/n\n')
        if answer == 'y':
            answer = raw_input('what type would you like? p/d/e\n')
            amount = int(raw_input('how many would you like?\n'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            elif answer == 'd':
                self.rent(self.diesel_cars, amount)
            elif answer == 'e':
                self.rent(self.electric_cars, amount)
            else:
                self.rent(self.hybrid_cars, amount)
        elif answer == 'n':
            amount = int(raw_input('How many cars are you returning?\n'))
        self.stock_count()
#need a return function
        
            
        
CarRental = CarRental()
CarRental.create_current_stock()
proceed = 'y'
while proceed == 'y':
    CarRental.process_rental()
    proceed = raw_input('continue? y/n\n')


    
    
