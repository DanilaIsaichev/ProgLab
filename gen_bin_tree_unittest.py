import unittest
import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(1, 4)), tuple({"4": [{"16": []}, {"5": []}]}))
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(2, 4)), tuple({'4': [{'16': [{'64': []}, {'17': []}]}, {'5': [{'20': []}, {'6': []}]}]}))
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(3, 4)), tuple({'4': [{'16': [{'64': [{'256': []}, {'65': []}]}, {'17': [{'68': []}, {'18': []}]}]}, {'5': [{'20': [{'80': []}, {'21': []}]}, {'6': [{'24': []}, {'7': []}]}]}]}))
        self.assertEqual(tuple(gen_bin_tree.gen_bin_tree(4, 4)), tuple({'4': [{'16': [{'64': [{'256': [{'1024': []}, {'257': []}]}, {'65': [{'260': []}, {'66': []}]}]}, {'17': [{'68': [{'272': []}, {'69': []}]}, {'18': [{'72': []}, {'19': []}]}]}]}, {'5': [{'20': [{'80': [{'320': []}, {'81': []}]}, {'21': [{'84': []}, {'22': []}]}]}, {'6': [{'24': [{'96': []}, {'25': []}]}, {'7': [{'28': []}, {'8': []}]}]}]}]}))


unittest.main(verbosity=1)
