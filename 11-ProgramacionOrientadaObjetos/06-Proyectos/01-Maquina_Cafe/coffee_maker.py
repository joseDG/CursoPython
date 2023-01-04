class CoffeeMaker:
    """Modelo de la maquina que hace el cafe"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Imprime un informe de todos los recursos"""
        print(f"Agua: {self.resources['water']}ml")
        print(f"Leche: {self.resources['milk']}ml")
        print(f"Cafe: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Devuelve True cuando se puede hacer el pedido, False si los ingredientes son insuficientes."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Lo siento, no hay suficiente{item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduce los ingredientes necesarios de los recursos"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui esta tu {order.name} ☕️. disfrutalo!")
