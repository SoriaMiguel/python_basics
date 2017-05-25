alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
# range() returns a set of numbers which tells Python how many times we want the loop to repeat
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change the color of the first three aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
# we use a slice to print the first 5
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
# print the length of the list to prove we've actually generated the full fleet
print("total number of aliens: " + str(len(aliens)))
