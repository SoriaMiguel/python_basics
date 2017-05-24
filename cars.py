# intro to python if statements
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

for car in cars:
    if car == "bmw" :
        print(car.upper())
    else:
        print(car.title())
