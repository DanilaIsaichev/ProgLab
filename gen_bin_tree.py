def gen_bin_tree(height, root):
    tree = {str(root): []}
    if height == 0:
        return tree
    left_leaf = root * 4
    right_leaf = root + 1
    height -= 1
    tree.get(str(root)).append(gen_bin_tree(height, left_leaf))
    tree.get(str(root)).append(gen_bin_tree(height, right_leaf))
    return tree


def gen_bin_tree_not_recursive(height, root):
    tree = {str(root): []}
    if height == 1:
        return tree
    else:
        leafs = [[root]]
        left_leaf = root
        right_leaf = root
        leafs.append([left_leaf * 4, right_leaf + 1])
        left_leaf *= 4
        right_leaf = right_leaf + 1
        for i in range(1, height+1):
            leafs.append([left_leaf * 4, left_leaf + 1])
            leafs.append([right_leaf * 4, right_leaf + 1])
            left_leaf *= 4
            right_leaf += 1
    return tree


def main():
    h = int(input("height = "))
    r = int(input("root = "))
    result = gen_bin_tree(height=h, root=r)
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
    print(gen_bin_tree_not_recursive(1, 4))
    print(gen_bin_tree_not_recursive(2, 4))
    print(gen_bin_tree_not_recursive(3, 4))
    print(gen_bin_tree_not_recursive(4, 4))
    print(gen_bin_tree(1, 4))
    print(gen_bin_tree(2, 4))
    print(gen_bin_tree(3, 4))
    print(gen_bin_tree(4, 4))
