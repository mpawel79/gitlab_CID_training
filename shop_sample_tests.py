import unittest


class ShopSampleTest(unittest.TestCase):

    def setUp(self):
        print("setUp")

        self.mock_actual_value = 'Lost Hat'



    def tearDown(self):
        print('tearDown')

    def testMainTitle(self):

        expected_value = 'Lost Hat'

        actual_value = self.mock_actual_value

        self.assertEqual(expected_value, actual_value)