import unittest

class TestConnect4:

    def setUp(self):

    def tearDown(self):

    def test_print_board(self):

    def test_check_win(self):

def suite():
    """Returns the suite of tests to run for this test class / module.
    Use unittest.makeSuite methods which simply extracts all of the
    methods for the given class whose name starts with "test"
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestConnect4))

    return test_suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())