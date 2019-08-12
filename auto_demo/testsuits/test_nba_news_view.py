# coding:utf-8
import unittest
import time
from auto_demo.fwork.browser_engine import BrowserEngine
from auto_demo.pageobjects.baidu_homepage import HomePage
from auto_demo.pageobjects.baidu_news_home import NewsHomePage
from auto_demo.pageobjects.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        # baiduhome.click_news()
        self.driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        # newshome.click_sports()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[7]/a")
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        # sportnewhome.click_nba_link()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]")
        sportnewhome.get_windows_img()


if __name__ == '__main__':
    unittest.main()
