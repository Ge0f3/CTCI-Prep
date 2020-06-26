import unittest
from collections import Counter

#O(N) solution
def compress(string): 
    res = ''
    count = 1
    for i in range(len(string)-1):
        if(string[i]==string[i+1]):
            count +=1
        else:
            res = res+string[i] + str(count)
            print(res)
            count = 1
    res = res+string[i] + str(count)

    if len(res)<len(string):
        return res
    else:
        return string

string = 'aabcccccaaa'

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
    print(compress(string))