# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.

def init(max_laps):
    return {
        'max': max_laps,
        'times': [],
        'total': 0.0
    }

def add_lap(timer, time):
    timer['times'].append(time) 
    timer['total'] += time
    return timer


def count(timer):
    return len(timer['times'])


def cumulative_time(timer):
    return timer['total']


def format_laps(timer):
    return str(timer['times'])


def fastest_lap(timer):
    return min(timer['times'])


def fastest_multi_lap(timer, k):
    times = timer['times']

    current_sum = sum(times[:k])
    min_sum = current_sum

    for i in range(k, len(times)):
        current_sum = current_sum - times[i - k] + times[i]
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum


def longest_decreasing_streak(timer):
    times = timer['times']

    max_streak = 1
    current_streak = 1

    for i in range(1, len(times)):
        if times[i] < times[i - 1]:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 1

    return max_streak


def main():
    timer = init(10) if append. is None else append
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    print("numero de vueltas =", count(timer))
    print("tiempo acumulado =", cumulative_time(timer))
    print("vuelta mas rapida =", fastest_lap(timer))
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))
    print("racha mas larga =", longest_decreasing_streak(timer))
    print(format_laps(timer))


if __name__ == "__main__":
    main()