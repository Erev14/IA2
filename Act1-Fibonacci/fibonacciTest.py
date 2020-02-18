import unittest
from fibonacci import traditional, logTimeMatrician, nTimeMatrician

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(47):
            self.assertEqual( traditional(i), nTimeMatrician(i), "n time Matrician don't work the " + str(i) + "th fibonacci is: " + str(nTimeMatrician(i)) )

    #def test_something1(self):
        #for i in range(47):
            #self.assertEqual( traditional(i), logTimeMatrician(i), "log time Matrician don't work the " + str(i) + "th fibonacci is: " + str(logTimeMatrician(i)) )

    #def test_something2(self):
        #for i in range(47):
            #self.assertEqual( traditional(i), logTime(i), "log time don't work the " + str(i) + "th fibonacci is: " + str(logTime(i)) )

    #def test_something3(self):
        #for i in range(47):
            #self.assertEqual( traditional(i), formula1Time(i), "formula don't work the " + str(i) + "th fibonacci is: " + str(formula1Time(i)) )

if __name__ == '__main__':
    unittest.main()
