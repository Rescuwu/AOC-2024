import unittest

class TestHelper(unittest.TestCase):
    def add_test(self, func, input_value, expected):
        """
        Add and execute a test for a given function.
        
        Args:
            func: The function to test.
            input_value: The input to the function. Can be a single value or a collection.
            expected: The expected result of the function.
        """
        inputs = (input_value,) if not isinstance(input_value, (tuple, list)) else input_value

        with self.subTest(func=func, input=input_value, expected=expected):
            result = func(*inputs)
            self.assertEqual(result, expected, f"Failed test with input={input_value}")

def run_tests(test_cases):
    """
    Dynamically create and execute tests based on provided test cases.

    Args:
        test_cases: A list of dictionaries with keys:
                    - 'func': Function to test
                    - 'tests': List of tuples (input_value, expected)
    """
    class DynamicTest(TestHelper):
        pass
    
    for case in test_cases:
        func = case['func']
        for i, (input_value, expected) in enumerate(case['tests']):
            def create_test(f=func, inp=input_value, exp=expected):
                def test(self):
                    self.add_test(f, inp, exp)
                return test

            test_name = f"test_{func.__name__}_{i}"
            setattr(DynamicTest, test_name, create_test())

    # Explicitly invoke the unittest test runner
    unittest.main()

