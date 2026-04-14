# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    filename = input("Nombre del archivo: ")

    with open(filename, 'r') as file:
        n = int(file.readline().strip())

        timer = lap_timer.init(n)

        for _ in range(n):
            time = float(file.readline().strip())
            timer = lap_timer.add_lap(timer, time)

    print(lap_timer.longest_decreasing_streak(timer))


if __name__ == "__main__":
    main()
