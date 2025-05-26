def min_platforms(robots: list[int], limit: int) -> int:

    '''
    Вычисляет минимальное количество платформ,
    необходимых для транспортировки роботов.

    Args:
        robots: принимает на вход массив целых чисел в первой строке
                через пробел — это вес отдельных роботов.

        limit:  принимает предельную грузоподъёмность платформы
                во второй строке.
    Returns:
        Целое число, указывающее на необходимое количество платформ
        для транспортировки.

    ID посылки: 138810434
    '''

    sorted_robots = sorted(robots)
    light_idx, heavy_idx = 0, len(robots) - 1
    platforms = 0

    while light_idx <= heavy_idx:
        if sorted_robots[light_idx] + sorted_robots[heavy_idx] <= limit:
            light_idx += 1
        heavy_idx -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    print(min_platforms([int(inputed_numbers) for
                         inputed_numbers in input().split()],
                        int(input())))
