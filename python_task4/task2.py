product = " фермерский ТВОРОГ " 
price = 4.567 
qty = 3 
csv_row = "milk,bread,cheese" 
review = "Это лучший ТВОРОГ в городе!" 
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

clean_product=product.strip().lower().title()

total=price*qty

print(f'Чек "EcoMarket"\nТовар: {clean_product}\nКол-во: {qty}\nИтого: {total}')

splited_csv_row=csv_row.split(',')
new_csw_row=" | ".join(splited_csv_row)
print(new_csw_row)

if "творог" in review.lower(): print(f"Отзыв относится к категории: Dairy {file_path}")
