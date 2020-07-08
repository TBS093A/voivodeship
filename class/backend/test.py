import unittest

from player import *
from country import *
from settlement import *

class TestCity(unittest.TestCase):

    playerTest = Player("playerTest", -1)
    countryTest = Country("countryTest", playerTest)
    provinceTest = Province("provinceTest", countryTest)

class TestCityTaxes(TestCity):

    def test_tax_0(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        self.provinceTest.respect = 100
        cityTest.taxesLevel = 0
        cityTest.people = 20
        cityTest.collectTaxes()
        self.assertEqual(self.provinceTest.respect, 100 - cityTest.taxesLevel)
        self.assertEqual(self.playerTest.gold, cityTest.people * cityTest.taxesLevel)

    def test_tax_1(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        self.provinceTest.respect = 100
        cityTest.taxesLevel = 1
        cityTest.people = 20
        cityTest.collectTaxes()
        self.assertEqual(self.provinceTest.respect, 100 - cityTest.taxesLevel)
        self.assertEqual(self.playerTest.gold, cityTest.people * cityTest.taxesLevel)

    def test_tax_2(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        self.provinceTest.respect = 100
        cityTest.taxesLevel = 2
        cityTest.people = 20
        cityTest.collectTaxes()
        self.assertEqual(self.provinceTest.respect, 100 - cityTest.taxesLevel)
        self.assertEqual(self.playerTest.gold, cityTest.people * cityTest.taxesLevel)

    def test_tax_3(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        self.provinceTest.respect = 100
        cityTest.taxesLevel = 3
        cityTest.people = 20
        cityTest.collectTaxes()
        self.assertEqual(self.provinceTest.respect, 100 - cityTest.taxesLevel)
        self.assertEqual(self.playerTest.gold, cityTest.people * cityTest.taxesLevel)

    def test_tax_4(self):
        cityTest = City("cityTest", self.provinceTest)
        self.playerTest.gold = 0
        self.provinceTest.respect = 100
        cityTest.taxesLevel = 4
        cityTest.people = 20
        cityTest.collectTaxes()
        self.assertEqual(self.provinceTest.respect, 100 - cityTest.taxesLevel)
        self.assertEqual(self.playerTest.gold, cityTest.people * cityTest.taxesLevel)

class TestCityFoodRations(TestCity):

    def test_food_rations_1(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 20
        cityTest.foodRationsLevel = 0
        cityTest.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 84)
        self.assertEqual(cityTest.food, { "apple": 20, "fish": 20, "chees": 20, "bread": 20 })

    def test_food_rations_2(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 20
        cityTest.foodRationsLevel = 1
        cityTest.food = { "apple": 0, "fish": 0, "chees": 0, "bread": 0 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 84)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 0, "bread": 0 })


    def test_food_rations_3(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 20
        cityTest.foodRationsLevel = 1
        cityTest.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 54)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 20, "chees": 20, "bread": 20 })


    def test_food_rations_4(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 20
        cityTest.foodRationsLevel = 1
        cityTest.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 100)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 20, "chees": 20, "bread": 20 })

    def test_food_rations_5(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 20
        cityTest.foodRationsLevel = 2
        cityTest.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 58)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 20, "bread": 20 })

    def test_food_rations_6(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 20
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 92)
        self.assertEqual(cityTest.food, { "apple": 10, "fish": 20, "chees": 20, "bread": 20 })

    def test_food_rations_7(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 20
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 5, "fish": 20, "chees": 20, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 92)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 15, "chees": 20, "bread": 20 })

    def test_food_rations_8(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 25, "fish": 12, "chees": 13, "bread": 20 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 92)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 0, "bread": 20 })

    def test_food_rations_9(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 0, "fish": 0, "chees": 0, "bread": 50 }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 92)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 0, "bread": 0 })

    def test_food_rations_10(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 0, "fish": 0, "chees": 25, "bread": 50 }
        cityTest.foodEatingBlock = { "apple": False, "fish": False, "chees": False, "bread": True }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 84)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 0, "bread": 50 })

    def test_food_rations_11(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.foodRationsLevel = 0.5
        cityTest.food = { "apple": 0, "fish": 0, "chees": 25, "bread": 50 }
        cityTest.foodEatingBlock = { "apple": False, "fish": False, "chees": True, "bread": False }
        cityTest.foodRations()
        self.assertEqual(self.provinceTest.respect, 92)
        self.assertEqual(cityTest.food, { "apple": 0, "fish": 0, "chees": 25, "bread": 0 })

class TestCityPeopleSatisfaction(TestCity):

    def test_entertainment_1(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 0
        cityTest.entertainment = { "beer": 20 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 100)
        self.assertEqual(cityTest.entertainment, { "beer": 20 })

    def test_entertainment_2(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 1
        cityTest.entertainment = { "beer": 20 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 100)
        self.assertEqual(cityTest.entertainment, { "beer": 20 })

    def test_entertainment_3(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 100
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 1
        cityTest.buildings.build((0,0), 'inn')
        cityTest.entertainment = { "beer": 20 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 100)
        self.assertEqual(cityTest.entertainment, { "beer": 0 })

    def test_entertainment_4(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 1
        cityTest.buildings.build((0,0), 'inn')
        cityTest.buildings.build((0,1), 'inn')
        cityTest.entertainment = { "beer": 20 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 50.5)
        self.assertEqual(cityTest.entertainment, { "beer": 0 })

    def test_entertainment_5(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 1
        cityTest.buildings.build((0,0), 'inn')
        cityTest.buildings.build((0,1), 'inn')
        cityTest.entertainment = { "beer": 400 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 60)
        self.assertEqual(cityTest.entertainment, { "beer": 200 })

    def test_entertainment_6(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 2
        cityTest.buildings.build((0,0), 'inn')
        cityTest.buildings.build((0,1), 'inn')
        cityTest.entertainment = { "beer": 400 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 55)
        self.assertEqual(cityTest.entertainment, { "beer": 0 })

    def test_entertainment_7(self):
        cityTest = City("cityTest", self.provinceTest)
        self.provinceTest.respect = 50
        cityTest.people = 100
        cityTest.peopleConsumptionLevel = 1
        cityTest.buildings.build((0,0), 'inn')
        cityTest.buildings.build((0,1), 'inn')
        cityTest.entertainment = { "beer": 0 }
        cityTest.peopleSatisfaction()
        self.assertEqual(self.provinceTest.respect, 50)
        self.assertEqual(cityTest.entertainment, { "beer": 0 })


if __name__ == '__main__':
    unittest.main() 