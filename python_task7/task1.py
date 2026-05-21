SMALL_BATCH_LIMIT = 500

def calculate_batch(weight, price, discount=0.0):
    ''''
    Рассчитать стоимость партии товара:
    weight - вес товара (кг)
    price - цена за кг
    discount - возможная скидка
    return - итоговая стоимость и флаг превышения лимита (кортеж)

    '''

    is_limit_exceeded=False
    final_sum=weight * price * (1 - discount)
    if final_sum> SMALL_BATCH_LIMIT:
        is_limit_exceeded=True
    return final_sum, is_limit_exceeded

carrot_batch=calculate_batch(100,4)
apple_batch=calculate_batch(50, 20, 0.1)

print(f"Партия 1 (Морковь): Сумма {carrot_batch[0]} Превышение лимита: {carrot_batch[1]}")
print(f"Партия 2 (Яблоки): Сумма {apple_batch[0]} Превышение лимита: {apple_batch[1]}")