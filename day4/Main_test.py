#from mylibs.test import run_test_cases
#from mylibs import test
#import unittest
#from mylibs.test import *
import mylibs.test 
from day4.Main import Part1

p1_test="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

testcasep1={
    "test" : [Part1(p1_test),18],
    "test1" : [1,1],
    "test2" : [2,2],
}
if __name__ == "__main__":
    pass
    #run_test_cases(testsmap=testcasep1)
    #test.run_test_cases(testcasep1)
    #print(globals())
    #unittest.main(verbosity=1)