import unittest

def Solution(A: list, K: int):
    if(all([isinstance(integer, int) for integer in A]) and len(A) in range(0,101) and K in range(0,101) and max(A, default=0) <= 1000 and min(A, default=0) >= -1000):
        if len(A) > 0:
            K = K % len(A)
        A.reverse()
        A[:K] = reversed(A[:K])
        A[K:] = reversed(A[K:])
        return A
    return 'failed'

class TestArrayRotation(unittest.TestCase):
    #test case from problem
    def test_array_rotation_success1(self):
        actual = Solution(A = [3, 8, 9, 7, 6], K = 3)
        expected = [9,7,6,3,8]
        self.assertEqual(actual,expected)
        
    #test case from problem
    def test_array_rotation_success2(self):
        actual = Solution(A = [0,0,0], K = 1)
        expected = [0,0,0]
        self.assertEqual(actual,expected)

    #test case from problem
    def test_array_rotation_success3(self):
        actual = Solution(A = [1,2,3,4], K = 4)
        expected = [1,2,3,4]
        self.assertEqual(actual,expected)

    def test_array_rotation_success_lenght_list_equal_0(self):
        actual = Solution(A = [] , K = 1)
        expected = []
        self.assertEqual(actual,expected)

    def test_array_rotation_success_lenght_list_equal_100(self):
        actual = Solution(A = list(range(1,101)) , K = 1)
        expected = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        self.assertEqual(actual,expected)

    def test_array_rotation_success_lenght_list_equal_99(self):
        actual = Solution(A = list(range(1,100)) , K = 1)
        expected = [99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
        self.assertEqual(actual,expected)

    def test_array_rotation_success_integer_equal_minus_1000_and_1000(self):
        actual = Solution(A = [-1000, 1000] , K = 1)
        expected = [1000, -1000]
        self.assertEqual(actual,expected)
    
    def test_array_rotation_success_integer_equal_minus_999_and_999(self):
        actual = Solution(A = [-999, 999] , K = 1)
        expected = [999, -999]
        self.assertEqual(actual,expected)

    def test_array_rotation_fail_by_list_have_more_than_100_integers(self):
        actual = Solution(A = list(range(1,102)), K = 1)
        expected = 'failed'
        self.assertEqual(actual, expected)

    def test_array_rotation_fail_by_K_more_than_100(self):
        actual = Solution(A = [3,8,9,7,6], K = 101)
        expected = 'failed'
        self.assertEqual(actual, expected)

    def test_array_rotation_fail_by_K_less_than_0(self):
        actual = Solution(A = [3,8,9,7,6], K = -1)
        expected = 'failed'
        self.assertEqual(actual, expected)
    
    def test_array_rotation_fail_by_integer_more_than_1000(self):
        actual = Solution(A = [1,2,3,1001], K = 1)
        expected = 'failed'
        self.assertEqual(actual, expected)
    
    def test_array_rotation_fail_by_integer_less_than_negative_1000(self):
        actual = Solution(A = [1,2,3,-1001], K = 1)
        expected = 'failed'
        self.assertEqual(actual, expected)
    
    def test_array_rotation_fail_by_K_is_not_integer(self):
        actual = Solution(A = [1,2,3,2000], K = 'A')
        expected = 'failed'
        self.assertEqual(actual, expected)

    def test_array_rotation_fail_by_integer_in_A_is_not_integer(self):
        actual = Solution(A = [1,2,3,'A'], K = 1)
        expected = 'failed'
        self.assertEqual(actual, expected)
    
    def test_array_rotation_fail_by_A_is_not_list(self):
        actual = Solution(A = 'a', K = 1)
        expected = 'failed'
        self.assertEqual(actual, expected)

unittest.main()