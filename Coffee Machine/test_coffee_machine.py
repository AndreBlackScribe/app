import unittest
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        self.coffee_machine = CoffeeMachine()
   
    def test_empty_input(self):
        """Test that empty input is handled properly"""
        result = self.coffee_machine.handle_user("")
        self.assertEqual(result, "No data entered! Input something.")
   
    def test_invalid_drink(self):
        """Test handling of invalid drink selection"""
        result = self.coffee_machine.handle_user("test123!")
        self.assertEqual(result, "No data entered! Input something.")
   
    def test_valid_drink_selection(self):
        """Test selecting a valid drink"""
        result = self.coffee_machine.handle_user("latte")
        self.assertEqual(result, "You chose latte")

    def test_water_usage(self):
        water = self.coffee_machine.resources["water"]
        # milk = self.coffee_machine.resources["milk"]
        # coffee = self.coffee_machine.resources["coffee"]
        self.coffee_machine.check_resources("latte")
        self.assertGreater(water, self.coffee_machine.resources["water"])
        

    def test_machine_shutdown(self):
        """Test machine shutdown command"""
        result = self.coffee_machine.handle_user("close")
        self.assertEqual(result, "You chose to turn off!")

    def test_sufficient_resources(self):
        """Test checking if there are enough resources for a drink"""
        result = self.coffee_machine.check_resources("latte")
        self.assertTrue(result)
   
    def test_insufficient_resources(self):
        """Test handling insufficient resources"""
        self.coffee_machine.resources["water"] = 50  # Not enough for a latte
        result = self.coffee_machine.check_resources("latte")
        self.assertFalse(result)
    
    def test_machine_report(self):
        """Test the print report command"""
        result =  self.coffee_machine
        self.assertTrue(result)

    def test_get_coin(self):
        """test if sufficient coins"""
        coins = 2
        result = self.coffee_machine.get_coins(coins)
        self.assertEqual(result, "You enterd 2 coins!")

    def test_insufficient_coins(self):
        coins = 1
        self.coffee_machine.get_coins(coins)
        result = self.coffee_machine.check_user_coins("latte")
        self.assertEqual(result, "1 is not enough! Your drink costs 2.5")


if __name__ == '__main__':
    unittest.main()