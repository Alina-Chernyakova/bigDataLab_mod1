
def calculate_purchase(product_name, weight:int , price:float):
    
    """
    Calculate the total cost of the lot and distribution index:
    :param product_name: string
    :param weight: int
    :param price: float
    
    """
    try:
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight

        print (f"Product: {product_name}. The total cost: {total_cost} ")
    except TypeError as e:
        print(f"Error type: {type(e)}")
        print(f"Message: {e}")
    except ValueError as e:
        print(f"Error type: {type(e)}")
        print(f"Message: {e}")
    except ZeroDivisionError as e :
        print(f"Error type: {type(e)}")
        print(f"Message: {e}")
    finally:
        print( "--- Batch varification completed ---" )

calculate_purchase("Томаты", 100, 2.5)
calculate_purchase("Огурцы","пятьдесят", 1.8)
calculate_purchase("Перец",0 , 4)
calculate_purchase("Зелень", [10],5)