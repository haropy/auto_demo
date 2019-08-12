# coding:utf-8
import unittest
from auto_demo.fwork.browser_engine import BrowserEngine
from auto_demo.pageobjects.baidu_homepage import HomePage


class GetPageTtitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())
