def make_pizza(size, *toppings):
    """Summarize the pizza we are making"""
    print(f"\nMaking a size {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')