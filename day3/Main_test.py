import unittest
from day3.Main import Part1,Part2





class TestDay3Main(unittest.TestCase):
    def test_part1(self):
        test="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result1 = Part1(test)
        self.assertEqual(result1, 161)  # Replace with actual expected result

    def test_part2(self):
        test2="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))dont"
        result2 = Part2(test2)
        self.assertEqual(result2, 48)
        test2=test2*1000
        result2 = Part2(test2)
        self.assertEqual(result2, 48000)
        test2= "don't()mul(2,3)do()mul(4,5)don't()mul(6,7)mul(8,9)"
        result2 = Part2(test2)
        self.assertEqual(result2, 20)
        test2="do()don't()do()mul(1,2)don't()do()mul(3,4)"
        result2 = Part2(test2)
        self.assertEqual(result2, 14)
        test2=("do()mul(1,1)" * 1000) + "don't()mul(2,2)"
        result2 = Part2(test2)
        self.assertEqual(result2, 1000)



if __name__ == "__main__":
    unittest.main()