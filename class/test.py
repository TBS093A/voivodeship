import unittest

from buildings import *

class TestCityEconomy(unittest.TestCase):

    playerTest = Player("playerTest", -1)
    countryTest = Country("countryTest", playerTest)
    provinceTest = Province("provinceTest", countryTest)

    def test_city_taxes_zero(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        cityTest.taxesLevel = 0
        cityTest.people = 20
        cityTest.taxes()
        self.assertEqual(cityTest.respect, 100)
        self.assertEqual(self.playerTest.gold, 0)

    def test_city_taxes_one(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        cityTest.taxesLevel = 1
        cityTest.people = 20
        cityTest.taxes()
        self.assertEqual(cityTest.respect, 99)
        self.assertEqual(self.playerTest.gold, 20)

    def test_city_taxes_two(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        cityTest.taxesLevel = 2
        cityTest.people = 20
        cityTest.taxes()
        self.assertEqual(cityTest.respect, 98)
        self.assertEqual(self.playerTest.gold, 40)

    def test_city_taxes_three(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        cityTest.taxesLevel = 3
        cityTest.people = 20
        cityTest.taxes()
        self.assertEqual(cityTest.respect, 97)
        self.assertEqual(self.playerTest.gold, 60)

    def test_city_taxes_four(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        cityTest.taxesLevel = 4
        cityTest.people = 20
        cityTest.taxes()
        self.assertEqual(cityTest.respect, 96)
        self.assertEqual(self.playerTest.gold, 80)

if __name__ == '__main__':
    unittest.main() 