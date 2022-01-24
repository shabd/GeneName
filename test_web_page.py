
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# inherit TestCase Class and create a new test class
class HomeTest(unittest.TestCase):
    web_address ="http://localhost:5000"
    file_path='/home/sha/Desktop/assessment/gene_name/gene_name.txt'
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    # Test case method. It should always start with test_
    def test_search_in_python_org(self):
         
        # get driver
        driver = self.driver
        driver.get(self.web_address)
        self.assertIn("File Upload", driver.title)

    def test_file_upload(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        driver.get(self.web_address)
        driver.find_element_by_xpath("//input[@type='file']").send_keys(self.file_path)
        driver.find_element_by_id("submit").click()

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()
