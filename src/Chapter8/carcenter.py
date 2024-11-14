# Exercises 8.14 and 8.17

def make_car(name, maker, **additional_info):
    '''Creates a register for new cars, saving every additional info.'''
    car = {}
    car['name'] = name
    car['maker']= maker
    for key, info in additional_info.items():
        car[key] = info
    return car

car = make_car('subaru', 'outback', color='blue', tow_package= True)
print(car)