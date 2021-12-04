import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class Handle_Dropdown(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print("this is.. browser set up..")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "http://cookbook.seleniumacademy.com/Config.html"
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("in the end, closing browser....")

    def setUp(self):
        print("setup before each method")

    def tearDown(self):
        print("teardown after each method")


    def test_combo(self):
        make_element = self.driver.find_element_by_name("make")
        make = Select(make_element)  # creating an object of type Select. Select constructors requires a parameter which is a
        # web element
        time.sleep(2)
        make.select_by_value("audi")  # select by the value attribute of the option element
        time.sleep(2)
        make.select_by_index(1)   # index starts from 0
        time.sleep(2)
        make.select_by_visible_text("Honda")
        time.sleep(3)
        selected_element = make.first_selected_option  # this gives you which option is currently selected.

        print("*first_selected_option-returns web element ", make.first_selected_option)

        print("Selected Element is -", selected_element.text)
        make.select_by_value("audi")

        selected_element = make.first_selected_option
        print("Last Selected Element is -", selected_element.text)
        # print("Is it a multiple Select? ", make.is_multiple)
        print("How many options are there inside combo?", len(make.options))

        print("Output of options attribute", type(make.options))
        print(make.options)
        expected_options = ["BMW", "Mercedes", "Audi", "Honda"]
        # print(make.options[0])
        # print(type(make.options[0]))
        # print(type(make.options[0].text))
        actual_options = []
        for option in make.options:
            actual_options.append(option.text)
        # print("Current Selected Option is - ", make.first_selected_option.text)
        self.assertListEqual(actual_options, expected_options)  # unittest - TestCase

    def test_multi_select(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        color_element = self.driver.find_element_by_name("color")
        make = Select(color_element)

        make.select_by_value("wt")
        time.sleep(2)
        # make.select_by_value("br")
        make.select_by_index(3)
        time.sleep(2)
        make.select_by_visible_text("Silver")
        time.sleep(2)

        print("No. of options selected", len(make.all_selected_options))
        expected_selected_colors = ["White", "Brown", "Silver"]
        actual_selected_colors = []
        for option in make.all_selected_options:
            actual_selected_colors.append(option.text)
        self.assertListEqual(actual_selected_colors, expected_selected_colors)

        make.deselect_by_visible_text("Brown")
        time.sleep(2)
        make.deselect_by_value("sl")
        make.deselect_all()


if __name__ == '__main__':
    unittest.main()
