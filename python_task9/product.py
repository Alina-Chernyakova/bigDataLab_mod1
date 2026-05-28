class Product:
    def __init__(self, name, price):
        self.name = name
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Цена должна быть положительной")

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Ошибка безопасности: Цена должна быть положительной!")

    def get_price(self):
        return self.__price
    
    def calculate_cost(self):
        return self.get_price()
        
    def get_display_info(self):
        return f"Товар: {self.name} | Цена: {self.get_price()} руб."