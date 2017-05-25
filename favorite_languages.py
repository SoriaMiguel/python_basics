favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python' 'haskel'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() +
#             ", I see your faorite language is " +
#             favorite_languages[name].title() + "!")

# looping through a dctionary's keys in order

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for takin ghte poll.")

#  Looping through all values in  a dictionary
#
# print("the following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# set is similar to a list except each item in the set must be unique
# print("The following languages hae been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())
