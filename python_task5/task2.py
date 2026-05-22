prices = [100, -50, 300, 40, 800]

prices.remove(-50)
prices.append(150)
prices.sort()
print(f"Базовый прайс (очищенный): {prices}")

tax_prices=[i *1.2 for i in prices]
print(f"Цены с НДС (>100): {tax_prices}")
print(f"Общая выручка: {sum(tax_prices)}")
print(f"Минимум: {min(tax_prices)}")
print(f"Максимум: {max(tax_prices)}")