def take_start_values(filename: str = 'in.txt') -> tuple[int, list[int]]:
    with open(filename, 'r') as fl:
        n, nums= fl.readlines()[:2]
    n = int(n)
    nums = list(map(int, nums.split(' ')))
    return n, nums

def write_ans_in_file(ans: str, filename: str = 'out.txt'):
    with open(filename, 'w') as fl:
        fl.write(str(ans))
    return True

def find_min_sectors(n: int, nums: list[int]) -> int:
    n = n - 1  # Так как первый элемент равен последнему и повторяется
    pi = [0] * n
    j = 0

    # Вычисление префикс-функции для числовой последовательности
    for i in range(1, n):
        while (j > 0 and nums[j] != nums[i]):
            j = pi[j - 1]
        if nums[j] == nums[i]:
            j += 1
        pi[i] = j

    min_sector_size = n - pi[n - 1] # минимальный размер сектора -- разница между n и максимальным значением
    return min_sector_size

ans = find_min_sectors(*take_start_values())
write_ans_in_file(ans)
