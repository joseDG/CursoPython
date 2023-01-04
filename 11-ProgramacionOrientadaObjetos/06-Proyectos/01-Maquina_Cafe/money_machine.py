class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "25 centavos": 0.25,
        "10 centavos": 0.10,
        "5 centavos": 0.05,
        "1 centavo": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Imprime el beneficio actual"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Devuelve el total calculando a partir de las monedas insertadas"""
        print("Porfavor inserte las monedas")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Cuantas {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Devuelve True cuando se acepta el pago, o False si es insuficiente"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Aquí está {self.CURRENCY}{change} tu cambio.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Lo siento, no es suficiente dinero")
            self.money_received = 0
            return False

