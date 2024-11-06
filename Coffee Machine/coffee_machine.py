class CoffeeMachine:
    def __init__(self):
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def handle_user(self, user_input):
        data = user_input.lower()
        try:
            match data:
                case "latte":
                    return "You chose latte"
                case "close":
                    return "You chose to turn off!"
                case _:
                    return "No data entered! Input something."
        except Exception as e:
            return f"Error handling client: {e}"

    def check_resources(self, drink):
        if drink not in self.MENU:
            return False
        
        for item, amount in self.MENU[drink]["ingredients"].items():
            if self.resources[item] < amount:
                return False
        return True