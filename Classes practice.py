import unittest
class Cars:
    def __init__(self, year, make, model, litre):
        self.year = year
        self.make = make
        self.model = model
        self.litre = litre
MyCar = Cars(1998, 'Jeep', 'Cherokee', 4)
FinleyCar = Cars(2023, 'Ford', 'F150', 2.7)
guess = input('Guess the car model')
class FunctionTest(unittest.TestCase):
    def Test_One(self):
        self.assertEquals(guess, MyCar.model)
unittest.main()
