favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'go'
}


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# To loop through just the key values:
for name in favorite_languages.keys():
   print( f"{name.title()}" )

print("\n")

# To loop in particular order:
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")

# To loop through all values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())