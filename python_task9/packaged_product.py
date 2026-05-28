from product import Product

class PackagedProduct(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = int(quantity)

    def calculate_cost(self):
        return self.get_price() * self.quantity
    
    def get_display_info(self):
        return f"Упаковка: {self.name} | Количество: {self.quantity} шт. | Итого: {self.calculate_cost()} руб."
    