# coding:utf-8
import unittest
import auto_demo.testsuits
from auto_demo.testsuits.test_baidu_search import BaiduSearch
from auto_demo.testsuits.test_get_page_title import GetPageTtitle

suite = unittest.TestLoader().discover("testsuits")
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# suite(unittest.makeSuite(GetPageTtitle))
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTtitle('test_get_title'))
if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
