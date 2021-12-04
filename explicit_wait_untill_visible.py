import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Explicit_Wait(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print("this is.. browser set up..")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://demoqa.com/dynamic-properties"
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("in the end, closing browser....")

    def test_element_visible(self):
        wait = WebDriverWait(self.driver, 20)
        button_visible = wait.until(expected_conditions.visibility_of_element_located((By.ID,"visibleAfter")))
        self.assertTrue(button_visible.is_displayed())


if __name__ == '__main__':
    unittest.main()