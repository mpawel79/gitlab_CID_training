import unittest


class ShopSampleTest(unittest.TestCase):

    def setUp(self):
        print("setUp")

        self.mock_acutal_title = 'Lost hat'



    def tearDown(self):
        print('tearDown')

    def testMainTitle(self):

        expected_value = 'Lost Hat'

        actual_value = self.mock_acutal_title

        self.assertEqual(expected_value, actual_value)