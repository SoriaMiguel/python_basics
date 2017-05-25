prompt = "\nPlease enter the city of a city you have visted:"
prompt += "\n(enter 'quit' when you are finished.) "


# while true will run forever until it reaches a break, at which point it will exit the loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
