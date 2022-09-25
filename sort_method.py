cars = ['bmw', 'audi', 'toyota', 'subaru']

# The sort() method, shown atu, changes the order of the list perma- nently.
# The cars are now in alphabetical order, and we can never revert to the original order
cars.sort()
print(cars)

# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
# The following example sorts the list of cars in reverse alphabetical order
cars.sort(reverse=True)
print(cars)
