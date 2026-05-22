raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "

splited_raw=raw_log.split('|')
order_id = splited_raw[0]
product_code=splited_raw[1]
raw_phone=splited_raw[2]
raw_city = splited_raw[3]

category=product_code[0:3]
region=product_code[-2:]

first_pos=product_code.find('-')
print(f"Позиция первого дефиса в коде товара: {first_pos}")

if product_code.startswith('FRT'): print("Код товара начинается с 'FRT'")
else: print("Код товара не начинается с 'FRT'")

clean_phone=""
for i in raw_phone:
    if i.isdigit(): 
        clean_phone +=i

print(f"Длина номера телефона: {len(clean_phone)} ")

clean_city=raw_city.strip().lower().title()

print(f"Заказ: {order_id}\nКатегория: {category} | Регион: {region}\nТелефон: {clean_phone}\nГород: {clean_city}")