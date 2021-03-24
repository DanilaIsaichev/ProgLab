import unittest
import gen_bin_tree


class TestGenBinTree14(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree_not_recursive(1, 4, lambda x: x * 4, lambda x: x + 1)), ([4], [16, 5]))


class TestGenBinTree24(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree_not_recursive(2, 4, lambda x: x * 4, lambda x: x + 1)), ([4], [16, 5], [64, 17, 20, 6]))


class TestGenBinTree34(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree_not_recursive(3, 4, lambda x: x * 4, lambda x: x + 1)), ([4], [16, 5], [64, 17, 20, 6], [256, 65, 68, 18, 80, 21, 24, 7]))


class TestGenBinTree44(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree_not_recursive(4, 4, lambda x: x * 4, lambda x: x + 1)), ([4], [16, 5], [64, 17, 20, 6], [256, 65, 68, 18, 80, 21, 24, 7], [1024, 257, 260, 66, 272, 69, 72, 19, 320, 81, 84, 22, 96, 25, 28, 8]))


if __name__ == '__main__':
    unittest.main()
