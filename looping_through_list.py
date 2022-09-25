magicians = ['alice', 'david', 'carolina']

# This line tells Python to retrieve the first value from the list magicians and associate it with the variable magician.
for magician in magicians:
    # Python prints the current value of magician, which is still 'alice'. Because
    # the list contains more values, Python returns to the first line of the loop
    # print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great show!")