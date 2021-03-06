from collections import deque


cars_on_wait = deque()

# During the green light cars will enter and exit the crossroads one by one
green_light_secs = int(input())

# During the free window cars will only exit the crossroads
free_window_secs = int(input())
total_passed_cars = 0
crash = False

while True:
    if crash:
        break

    data = input()

    if data == 'END':
        print('Everyone is safe.')
        print(f'{total_passed_cars} total cars passed the crossroads.')
        break

    if data == 'green':
        is_green = True
        passed_seconds_on_green = 0

        while is_green:

            if passed_seconds_on_green == green_light_secs or not cars_on_wait:
                is_green = False
                break

            crossing_car = cars_on_wait.popleft()
            left_green_seconds = green_light_secs - passed_seconds_on_green
            if len(crossing_car) <= left_green_seconds:
                total_passed_cars += 1
                passed_seconds_on_green += len(crossing_car)
            else:
                is_green = False
                total_left_seconds = left_green_seconds + free_window_secs
                if len(crossing_car) <= total_left_seconds:
                    total_passed_cars += 1
                else:
                    previous_car = crossing_car
                    crossing_car = list(crossing_car)
                    while total_left_seconds:
                        crossing_car.pop(0)
                        total_left_seconds -= 1
                    crash = True
                    print('A crash happened!')
                    print(f'{previous_car} was hit at {crossing_car[0]}.')
    else:
        cars_on_wait.append(data)

########################### SECOND SOLUTION #########################


green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
passed_cars = 0
while True:
    command = input()

    if command == 'END':
        print('Everyone is safe.')
        print(f'{passed_cars} total cars passed the crossroads.')
        break
    elif command == 'green':
        green_light = green_light_duration
        while cars and green_light >= len(cars[0]):
            green_light -= len(cars.popleft())
            passed_cars += 1
            
        if green_light and cars:
            total_time = green_light + free_window_duration
            if total_time >= len(cars[0]):
                cars.popleft()
                passed_cars += 1
            else:
                crashing_car = deque(cars.popleft())
                whole_car = ''.join(crashing_car.copy())
                while total_time:
                    total_time -= 1
                    crashing_car.popleft()
                print('A crash happened!')
                print(f'{whole_car} was hit at {crashing_car.popleft()}.')
                break
    else:
        cars.append(command)
