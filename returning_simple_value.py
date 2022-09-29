def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('davey', 'havok')
print(musician)

musician = get_formatted_name('stevie', 'vaughn', 'ray')
print(musician)

# the name is built from three possible parts.
# Because there’s always a first and last name,
# these parameters are listed first in the function’s definition.
# The middle name is optional, so it’s listed last in the definition,
# and its default value is an empty string
