# _*_ coding:utf-8 _*_

# 把100赋值给cars
cars = 100
# 把4.0赋值给space_in_car
space_in_a_car = 4.0
# 把30赋值给drivers
drivers = 30
# 把90赋值给passengers
passengers = 90
# 把cars - drivers的值赋值给car_not_driven
cars_not_driven = cars - drivers
# 把drivers的值赋值给cars_driven
cars_driven = drivers
# 把cars_driven * space_in_a_car的值赋值给carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# 把passengers / cars_driven的值赋值给average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# 打印输出There are 100 cars available.
print "There are",cars, "cars available."
# 打印输出There are only 30 drivers avaolable.
print "There are only", drivers, "drivers avaolable."
# 打印输出There will be 70 empty cars today.
print "There will be",cars_not_driven, "empty cars today."
# 打印输出we can transport 120.0 people today.
print "we can transport",carpool_capacity, "people today."
# 打印输出we have 90 to carpool_capacity today.
print "we have", passengers,"to carpool_capacity today."
# 打印输出we need to put about (3) in each car.
print "we need to put about", average_passengers_per_car, "in each car."