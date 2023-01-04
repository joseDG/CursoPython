class MenuItem:
    """Modelos para escoger del Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Modelo con el menu de bebidas."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.50),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.50),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.00),
        ]

    def get_items(self):
        """Retornamos todos los items del menu """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Busca en el menu una bebida en particular por nombre.Devulve ese elemento si existe, de lo contrario devuleve ninguno"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Lo sentimos, ese articulo no esta disponible.")
