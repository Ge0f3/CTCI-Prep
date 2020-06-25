import unittest

#O(N) solution with extra storage 
def reversestr(string):
    rev_str = ''

    for chr in reversed(string):
        rev_str += chr

    return rev_str

#recursion 0(N) without any extra storage 
def reversestrRec(string):
    if string != '':
        return str[-1:] + reversestrRec(str[:-1])
    else:
        return ""
    
    


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