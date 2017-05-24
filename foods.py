# copying a list
# copy a list with an empty slice
# without a slice, we would only be setting the variable the same as one another and changes to one would be reflected
# in both which isn't what we want
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMyfriend's favorite foods are:")
print(friend_foods)
