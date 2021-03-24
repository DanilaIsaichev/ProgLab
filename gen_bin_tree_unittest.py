import unittest
import gen_bin_tree


class TestGenBinTree14(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(1, 4, lambda x: x * 4, lambda x: x + 1)), tuple({"4": [{"16": []}, {"5": []}]}))

class TestGenBinTree24(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(2, 4, lambda x: x * 4, lambda x: x + 1)), tuple({'4': [{'16': [{'64': []}, {'17': []}]}, {'5': [{'20': []}, {'6': []}]}]}))

class TestGenBinTree34(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(3, 4, lambda x: x * 4, lambda x: x + 1)), tuple({'4': [{'16': [{'64': [{'256': []}, {'65': []}]}, {'17': [{'68': []}, {'18': []}]}]}, {'5': [{'20': [{'80': []}, {'21': []}]}, {'6': [{'24': []}, {'7': []}]}]}]}))

class TestGenBinTree44(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(4, 4, lambda x: x * 4, lambda x: x + 1)), tuple({'4': [{'16': [{'64': [{'256': [{'1024': []}, {'257': []}]}, {'65': [{'260': []}, {'66': []}]}]}, {'17': [{'68': [{'272': []}, {'69': []}]}, {'18': [{'72': []}, {'19': []}]}]}]}, {'5': [{'20': [{'80': [{'320': []}, {'81': []}]}, {'21': [{'84': []}, {'22': []}]}]}, {'6': [{'24': [{'96': []}, {'25': []}]}, {'7': [{'28': []}, {'8': []}]}]}]}]}))


if __name__ == '__main__':
    unittest.main()
