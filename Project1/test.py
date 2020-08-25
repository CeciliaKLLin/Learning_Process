import unittest

import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    # it allow to a piece of code that set up before each call of the test

    def test_do_stuff(self):
        '''HIHIHI'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'gerfer'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')



    def tearDown(self): #at the bottom of each call of test
        print('clearing up')

if __name__ == '__main__':
    unittest.main()