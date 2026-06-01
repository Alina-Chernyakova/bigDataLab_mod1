SMALL_BATCH_LIMIT = 500

def calculate_batch(weight: int, price: int, discount=0.0)->tuple:
    """
    Рассчитать стоимость партии товара:
    :param weight - вес товара (кг), int
    :param price - цена за кг, int
    :param discount - возможная скидка, float
    :param return - итоговая стоимость и флаг превышения лимита (tuple)

    """

    
    final_sum=weight * price * (1 - discount)
    is_limit_exceeded= final_sum >SMALL_BATCH_LIMIT
    
    return final_sum, is_limit_exceeded

carrot_sum, carrot_exceeded=calculate_batch(100,4)
apple_sum, apple_exceeded=calculate_batch(50, 20, 0.1)

print(f"Партия 1 (Морковь): Сумма {carrot_sum} Превышение лимита: {carrot_exceeded}")
print(f"Партия 2 (Яблоки): Сумма {apple_sum} Превышение лимита: {apple_exceeded}")