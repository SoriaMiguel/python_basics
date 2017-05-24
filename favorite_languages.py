favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your faorite language is " +
            favorite_languages[name].title() + "!")


a.each_with_index.map do |x,i|
    if (x+i) == 0
        0
    else (x+i)/2
    end
end
