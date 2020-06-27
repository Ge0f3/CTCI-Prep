import unittest


#O(MxN) solution with additional memory

def setZero(matrix):

    row , cols = set(), set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]) == 0:
                row.add(i)
                cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row or j in cols:
                matrix[i][j] = 0

   
matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
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
    setZero(matrix)
    print(matrix)