from coffee_machine import CoffeeMachine
from test_coffee_machine import TestCoffeeMachine

def main():
    # Create an instance of TestCoffeeMachine
    test_suite = TestCoffeeMachine('setUp')
    
    # Run specific tests
    test_suite.setUp()
    test_suite.test_empty_input()
    test_suite.test_invalid_drink()
    test_suite.test_valid_drink_selection()
    test_suite.test_machine_shutdown()
    test_suite.test_sufficient_resources()
    test_suite.test_insufficient_resources()
    test_suite.test_machine_report()
    test_suite.test_get_coin()


if __name__ == "__main__":
    main()