import unittest
from week4 import rainaverage

class TestWeek4(unittest.TestCase):
    def test_avgrain(self):
        case1 = [(1,2),(1,3),(2,3),(1,1),(3,8)] 
        case2 = [('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)] 

        case1_output = [(1, 2.0), (2, 3.0), (3, 8.0)]
        case2_output = [('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]

        self.assertEqual(rainaverage(case1), case1_output)
        self.assertEqual(rainaverage(case2), case2_output)

if __name__ == "__main__":
    unittest.main()

