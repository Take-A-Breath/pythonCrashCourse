dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# The lines starting atudefine the original tuple and print the initial dimensions.
# We associate a new tuple with the variable dimensions. We then print the new dimensions.
# Python doesn’t raise any errors this time, because reassigning a variable is valid
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)