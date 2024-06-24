import unittest
from function import sequence

class test(unittest.TestCase):
    #n에 대한 올바른 Ln이 나오는지 확인
    def test_sequence(self):
        testcase = [
            (1, "1"),
            (2, "11"),
            (3, "21"),
            (4, "1211"),
            (5, "111221"),
            (6, "312211"),
            (7, "13112221"),
            (8, "1113213211"),
        ]
        
        for n, output in testcase:
            self.assertEqual(sequence(n), output)
    