# removing all instances of a specific item form a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# positional arguments

def describe_pet(pet_name,animal_type='dog'):
    # a pet name must always be given but unless otherwise specified, the devault type will be dog
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
# calling style can be either "pet_name='willie'" or just 'willie', it doesn't matter
