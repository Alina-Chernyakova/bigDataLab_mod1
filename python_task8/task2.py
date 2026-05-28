from typing import Union, Optional

def calculate_total_delivery_cost(product_name, weights: Union[list,tuple], 
                                  prices: Union[list,tuple], discount: Optional[float] = None,
                                    currency_rate: float | int = 1, *extra_costs: float|int)->dict[str,float]:

   """
    Calculate the final cost of a batch of goods taking into account base prices, discounts and additional costs
    
    :param product_name: string
    :param weights: list or tuple
    :param prices: list or tuple
    :param discount: float or none
    :currency_rate: int or float
    :return: dict[str, float]

   """

   if len(weights) != len(prices):
        raise ValueError("Number of element doesn't match")
   
   total_sum: float | int = 0
   discount_sum: float
   extra_sum: float | int
   final_sum: float

     
   for i in range(len(weights)):
    total_sum += weights[i] * prices[i]
    
   discount_sum = float(total_sum)
   if discount is not None:
        discount_sum = total_sum * (1 - discount)

   extra_sum = sum(extra_costs)
   final_sum = (discount_sum + extra_sum)*currency_rate

   return {product_name: final_sum}

def print_report(report_dict: dict[str, float]) -> None:
    for product_name, total_cost in report_dict.items():
        print(f"Товар: {product_name}, итоговая стоимость: {total_cost}")

result_vegetables = calculate_total_delivery_cost("Овощная партия", [100, 50],[4, 6],0.1, 1,20,15)
result_fruits = calculate_total_delivery_cost("Фруктовая партия", (30, 20, 10),(15, 12, 18),None,1.2,25)

print_report(result_vegetables)
print_report(result_fruits)

