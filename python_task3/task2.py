total_revenue = 0

daily_logs = [
    [500, 0, 1200],       
    [300, -999, 800],     
    [1500, 200]           ]

for index, value in enumerate(daily_logs,start=1):
    print (f"--- Обработка Кассы №{index} ---")
    for i, v in enumerate(value):
        if v== -999 :
            print("Аварийная остановка кассы!")
            break
        elif v==0 :
            print("Сбой (0)")
            continue
        elif v>=0:
            print(f"Добавлено: {v}")
            total_revenue+=v

print("=== ИТОГ ДНЯ ===")
print(f"Общая выручка магазина: {total_revenue}")