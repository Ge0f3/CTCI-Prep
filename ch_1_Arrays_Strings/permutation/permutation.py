import unittest
from collections import Counter

#O(NlogN) solution with sorting
def permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

#recursion 0(N) with an extra storage 
def permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    counter = Counter()
    for c in s1:
        counter[c] += 1
    for c in s2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
    


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