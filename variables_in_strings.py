first_name = 'norman'
last_name = 'bates'

# These strings are called f-strings. The f is for format, because Python formats the string
# by replacing the name of any variable in braces with its value.
full_name = f"{first_name} {last_name}"
print(full_name)

# The full name is used in a sentence that greets the user, and the title() method changes the name to title case.
# This code returns a simple but nicely formatted greeting:
print(f"Hello, {full_name.title()}!")

# You can also use f-strings to compose a message, and then assign the entire message to a variable:
message = f"Hello, {full_name.title()}!"
print(message)