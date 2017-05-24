# alien_0 = {'color' : 'green', 'points' : 5}
# # print(alien_0['color'])
# # print(alien_0['points'])
#
# # new_points = alien_0['points']
# # print("You just earned " + str(new_points) + " points!")
#
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# starting empty
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x-positition: " + str(alien_0['x_position']))
# Move the alien tot he right.
# Determine how far to move th alien based on tis current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3

# The new postion is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] +x_increment

print("New x-position: " + str(alien_0['x_position']))
