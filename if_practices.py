cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car.startswith('a'):
        print(car)

cars.remove('audi')
cars.append('xiaomi')
if 'audi' in cars:
    print(f"found {'audi'.title()}")
elif 'nissan' not in cars:
    print(f"don't have {'nissan'.upper()}")
