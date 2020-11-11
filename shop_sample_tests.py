import unittest

import  platform
from selenium import webdriver

class ShopSampleTest(unittest.TestCase):

    def setUp(self):
        print("setUp")

        if platform.uname()[0] == 'Darwin':
            print("Darwin - local")
            self.driver = webdriver.Chrome(executable_path=r'libs/chromedriver')

        else:

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')

            #self.driver = webdriver.Chrome(options=chrome_options)
            self.driver = webdriver.Chrome(options=chrome_options)

        self.base_url = 'https://autodemo.testoneo.com/en/'

    def tearDown(self):
        print('tearDown')
        self.driver.quit()

    def testMainTitle(self):

        self.driver.get(self.base_url)

        expected_value = 'Lost Hat'
        actual_value = self.driver.title

        self.assertEqual(expected_value, actual_value)