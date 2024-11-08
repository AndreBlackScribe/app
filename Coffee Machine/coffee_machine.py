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
        self.user_coins = 0

    def handle_user(self, user_input):
        data = user_input.lower()
        try:
            match data:
                case "latte":
                    return "You chose latte"
                case "close":
                    return "You chose to turn off!"
                case "report":
                    return self.resources
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
            else:
                self.resources[item] -= amount
        return True
    
    def check_user_coins(self, drink):
        cost = self.MENU[drink]["cost"]
        if self.user_coins >= cost:
            return True
        else:
            return f"{self.user_coins} is not enough! Your drink costs {cost}"
    

    def get_coins(self, user_coins):
        try:
            self.user_coins = user_coins
            return f"You enterd {self.user_coins} coins!"
        except Exception as e:
            return f"Error handling client: {e}"
        