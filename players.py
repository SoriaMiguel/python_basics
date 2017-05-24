# slice function give it a range of indexes
# if no first index position is given, it'll start at the beginning and stop at the given range position
# if no second index position is given, it'll start at the position given and work to the end
# ranges always go up to (but do not include)the terminating index
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
