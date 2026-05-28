from product import Product
from weighable_product import WeighableProduct
from packaged_product import PackagedProduct

cart=[]
cart.append(Product("Молоко", 100))
cart.append(WeighableProduct("Яблоки", 50, 2.5))
cart.append(PackagedProduct("Яйца", 12, 10))

cart[0].set_price(-200)

print("\n--- Чек EcoMarket ---")

total_cost = 0  
for item in cart:
    print(item.get_display_info())
    total_cost += item.calculate_cost()

print("---------------------")
print(f"ИТОГО К ОПЛАТЕ: {total_cost:.1f} руб.")