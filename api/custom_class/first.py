from itertools import combinations


def find_triplets_set(nums: list) -> list[list]:
    """
    Поиск триплетов, которые в произведении дает 0
    Сложность алгоритма:
        combinations => O(C(n, 3)) = n! / 3! / (n-3)!
        set.add => O(1) с проверкой уникальности
        set to list => O(n! / 3! / (n-3)!) - кол-во элементов n! / 3! / (n-3)!

    :param nums: массив для поиска
    :return: список триплетов, произведение которых = 0
    """
    return list(map(lambda x: list(x), set(
        combo
        for combo in combinations(nums, 3)
        if 0 in combo
    )))
