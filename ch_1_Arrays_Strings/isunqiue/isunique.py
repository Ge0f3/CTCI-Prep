import unittest

#O(N) solution with hash map
def isuniques(string):
    #Assuming ASCII not unicode the possible combination of unique char is 256 2^7 ; unicode 0-2^21
    if len(string) > 256:
        return False
    
    chardic ={}

    for ch in string:
        if ch in chardic:
            return False
        else:
            chardic[ch] = True
    
    return True


def isunique(string):
    
    if len(string) >256:
        return False
    
    checker = 0 

    for char in string:

        if checker & (1<<ord(char)):
            return False
        
        checker |= (1<<ord(char))
    
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