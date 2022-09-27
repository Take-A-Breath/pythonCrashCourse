alien_0 = {'color': 'green', 'speed': 'slow'}

# Can't print values if the key pair doesn't exist
# print(alien_0['points'])

# The get() method requires a key as a first argument.
# As a second optional argument, you can pass the value to be returned
# if the key doesn’t exist:
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)