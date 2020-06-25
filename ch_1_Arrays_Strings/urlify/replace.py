import unittest
from collections import Counter

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string



class Test(unittest.TestCase):

    str1 = [('abcd'), ('s4fad'), ('')]
    str2 = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):

        for test_string in self.str1:
            res = isunique(test_string)
            self.assertTrue(res)
        
        for test_string in self.str2:
            res = isunique(test_string)
            self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()