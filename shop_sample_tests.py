import unittest


class ShopSampleTest(unittest.TestCase):

    def setUp(self):
        print("setUp")



    def tearDown(self):
        print('tearDown')

    def testMainTitle(self):

        expected_value = 'Lost Hat'

        actual_value = 'Lost Hat'

        self.assertEqual(expected_value, actual_value)