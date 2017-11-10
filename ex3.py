# Number of cars
cars = 100
# Space available in each car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# cars which are not going to be driven
cars_not_driven = cars - drivers
# cars which will be driven
cars_driven = drivers
# It will check the amount of available sits
carpool_capacity = cars_driven * space_in_a_car
# It will calculate the average of passengers
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
