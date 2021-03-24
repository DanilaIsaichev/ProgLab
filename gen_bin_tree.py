def gen_bin_tree(height, root, left_leaf_funct, right_leaf_funct):
    tree = {str(root): []}
    if height == 0:
        return tree
    left_leaf = left_leaf_funct(root)
    right_leaf = right_leaf_funct(root)
    height -= 1
    tree.get(str(root)).append(gen_bin_tree(height, left_leaf, left_leaf_funct, right_leaf_funct))
    tree.get(str(root)).append(gen_bin_tree(height, right_leaf, left_leaf_funct, right_leaf_funct))
    return tree


def gen_bin_tree_not_recursive(height, root, left_leaf_funct, right_leaf_funct):
    tree = {str(root): []}
    if height == 0:
        return tree

    tree = [[0] * 2 ** (i - 1) for i in range(1, height + 2)]
    tree[0][0] = root

    for i in range(1, height + 1):
        for j in range(0, len(tree[i]), 2):
            k = j // 2
            tree[i][j] = left_leaf_funct(tree[i - 1][k])
            tree[i][j + 1] = right_leaf_funct(tree[i - 1][k])
    return tree


def main():
    h = int(input("height = "))
    r = int(input("root = "))
    result = gen_bin_tree(h, r, lambda x: x * 4, lambda x: x + 1)
    print(result)
    return result


if __name__ == '__main__':
    # h = 1
    example1 = {
        "4": [{
            "16": []
        },{
            "5": []
        }
    ]}
    #h = 2
    example2 = {
        "4": [{
            "16": [{
                "64": []
            },{
                "17": []
            }]
        },{
            "5": [{
                "20": []
            },{
                "6": []
            }
        ]}
    ]}
    print("Бинарное дерево с корнем 4 и глубиной 1 (не рекурсия)")
    print(gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1))

    print("Бинарное дерево с корнем 4 и глубиной 1 (рекурсия)")
    print(gen_bin_tree(1, 4, lambda x: x * 4, lambda x: x + 1))

    print("\nБинарное дерево с корнем 4 и глубиной 2 (не рекурсия)")
    print(gen_bin_tree_not_recursive(2, 4, lambda x: x * 4, lambda x: x + 1))

    print("Бинарное дерево с корнем 4 и глубиной 2 (рекурсия)")
    print(gen_bin_tree(2, 4, lambda x: x * 4, lambda x: x + 1))

    print("\nБинарное дерево с корнем 4 и глубиной 3 (не рекурсия)")
    print(gen_bin_tree_not_recursive(3, 4, lambda x: x * 4, lambda x: x + 1))

    print("Бинарное дерево с корнем 4 и глубиной 3 (рекурсия)")
    print(gen_bin_tree(3, 4, lambda x: x * 4, lambda x: x + 1))

    print("\nБинарное дерево с корнем 4 и глубиной 4 (не рекурсия)")
    print(gen_bin_tree_not_recursive(4, 4, lambda x: x * 4, lambda x: x + 1))

    print("Бинарное дерево с корнем 4 и глубиной 4 (рекурсия)")
    print(gen_bin_tree(4, 4, lambda x: x * 4, lambda x: x + 1))
