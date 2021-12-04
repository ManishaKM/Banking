import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# comment added

class Handle_Drag_Drop(unittest.TestCase):
    driver2 = None

    @classmethod
    def setUpClass(cls):
        print("this is.. browser set up..")
        cls.driver2 = webdriver.Chrome(ChromeDriverManager().install())
        url_double_click = "http://www.cookbook.seleniumacademy.com/DoubleClickDemo.html"
        cls.driver2.get(url_double_click)

        # cls.driver2.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver2.quit()
        print("in the end, closing browser....")

    def test_01_double_click(self):
            message = self.driver2.find_element_by_id("message")
            # verify blue color
            self.assertEqual("rgba(0, 0, 255, 1)", message.value_of_css_property("background-color"))
            # self.assertEqual("rgba(0, 0, 255, 1)", message.get_property("background-color"))  # this is useful for generic properties/ attributes
            actions = ActionChains(self.driver2)
            # time.sleep(2)
            actions.double_click(message).perform()
            time.sleep(2)
            self.assertEqual("rgba(255, 255, 0, 1)", message.value_of_css_property("background-color"))


if __name__ == '__main__':
    unittest.main()