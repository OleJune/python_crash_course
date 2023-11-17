import car

car.car_profile('audi', 'a5', color='silver', year='2020')

print("------")

from car import car_profile

print(car_profile('audi', 'a5', color='white', year='2021'))

print("------")

from car import car_profile as cp

print(cp('audi', 'a5', color='black', year='2022'))

print("------")

import car as c

print(c.car_profile('audi', 'a5', color='red', year='2019'))

print("------")

from car import *

print(car_profile('audi', 'a5', color='blue', year='2023'))
