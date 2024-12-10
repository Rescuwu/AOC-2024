import unittest
from day6.Main import Part1

class TestDay06Main(unittest.TestCase):
    def test_part1(self):
        test=open("day6/p1").read()

        self.assertEqual(Part1(test)+1,41)


if "__main__" == __name__:
    unittest.main()