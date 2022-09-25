# amusement_park.py
age = 12

# The if test atutests whether a person is under 4 years old.
# If the test passes, an appropriate message is printed and Python skips the rest of the tests.
if age < 4:
    print("Your admission cost is $0")

# The elif line is really another if test, which runs only if the previous test failed.
# At this point in the chain, we know the person is at least 4 years old because the first test failed.
# If the person is under 18, an appro - priate message is printed and Python skips the else block.
elif age < 18:
    print("Your admission cost is $25")

# Any age greater than 17 would cause the first two tests to fail. In these situations,
# the else block would be executed and the admission price would be $40.
else:
    print("Your admission cost is $40")