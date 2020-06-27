import unittest


#O(N^2) solution


def rotate(matrix): 

    n = len(matrix[0])
    for i in range(n):
        for j in range(i,n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i].reverse()
   

matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
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
    rotate(matrix)
    print(matrix)