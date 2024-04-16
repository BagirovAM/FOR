cars_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(cars_.__len__()):
    print(f'Я езжу на автомобиле марки {cars_[i]}')
    cars_count += 10
    print(f'cars_count = {cars_count}')