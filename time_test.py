import timeit
import gen_bin_tree

if __name__ == '__main__':
    print("\nТест времени для глубины 1:")
    print("Рекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree(1, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)
    print("Нерекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree",number=100)) * 1000)

    print("\nТест времени для глубины 2:")
    print("Рекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree(2, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)
    print("Нерекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)

    print("\nТест времени для глубины 3:")
    print("Рекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree(3, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)
    print("Нерекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)

    print("\nТест времени для глубины 4:")
    print("Рекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree(4, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree", number=100)) * 1000)
    print("Нерекурсивное решение:")
    print(min(timeit.repeat("gen_bin_tree.gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1)", "from __main__ import gen_bin_tree",number=100)) * 1000)
