#:coding:utf-8
from auto_demo.fwork.base_page import BasePage


class SportNewsHomePage(BasePage):
    # NBA入口
    sports_link = "xpath=>//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
