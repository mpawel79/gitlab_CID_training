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

        contact_us_page = 'https://autodemo.testoneo.com/en/contact-us'
        self.driver.get(contact_us_page)

        expected_value = 'Contact us'
        actual_value = self.driver.title

        self.assertEqual(expected_value, actual_value)

    def test_contact_us_invalid_email_error_for_empty_email(self):
        contact_us_page = 'https://autodemo.testoneo.com/en/contact-us'
        expected_title = 'Invalid email address.'
        self.driver.get(contact_us_page)
        self.driver.find_element_by_css_selector('.form-footer > .btn').click()
        error = self.driver.find_element_by_css_selector('.alert.alert-danger > ul > li')

        self.driver.get_screenshot_as_file("testResults/screenshot_invalid_contact.png")

        self.assertEqual(expected_title, error.text)
