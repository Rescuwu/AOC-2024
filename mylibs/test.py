import unittest

class DynamicClassBase(unittest.TestCase):
    longMessage = True

def make_test_function(description, a, b):
    def test(self):
        self.assertEqual(a, b, description)
    return test

def run_test_cases(testsmap,verbosity=1):
    print(testsmap)
    for name, params in testsmap.items():  # Changed from iteritems() to items() for Python 3
        test_func = make_test_function(name, params[0], params[1])
        klassname = 'Test_{0}'.format(name)
        globals()[klassname] = type(klassname,
                                   (DynamicClassBase,),
                                   {'test_gen_{0}'.format(name): test_func})

    unittest.main(verbosity=verbosity)


#if __name__ == '__main__':
if True:    
    testsmap = {
        'foo': [1, 1],
        'bar': [1, 2],
        'baz': [5, 5]
    }
    testsmap={
    "test" : [18,18],
    "test1" : [1,1],
    }
    run_test_cases(testsmap)
    """
    for name, params in testsmap.items():  # Changed from iteritems() to items() for Python 3
        test_func = make_test_function(name, params[0], params[1])
        klassname = 'Test_{0}'.format(name)
        globals()[klassname] = type(klassname,
                                   (DynamicClassBase,),
                                   {'test_gen_{0}'.format(name): test_func})

    unittest.main(verbosity=1)"""
