import unittest
from collections import Counter

#O(N) solution
def isSubstr(s1,s2):
    return s1.find(s2)>-1

def isRotation(s1,s2): 

    s1 = s1+s1

    return isSubstr(s1,s2)
   

s1 = 'waterbottle'
s2 = 'bottle'

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
    print(isRotation(s1,s2))