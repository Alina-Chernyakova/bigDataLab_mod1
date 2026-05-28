from product import Product

class WeighableProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    
    def calculate_cost(self):
        return self.get_price() * self.weight
    
    def get_display_info(self):
        return f"Весовой товар: {self.name} | Вес: {self.weight} кг | Итого: {self.calculate_cost()} руб."