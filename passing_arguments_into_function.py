def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments allow you to avoid confusion in positional arguments:
describe_pet(animal_type='dog', pet_name='akuma')

# The function describe_pet() hasn’t changed.
# But when we call the function, we explicitly tell Python
# which parameter each argument should be matched with.
# When Python reads the function call, it knows to assign the argument
# 'dog' to the parameter animal_type and the argument 'akuma' to pet_name.
