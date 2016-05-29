import sys
import nose
import unittest
from Plugins.htmlReport import HtmlOutput

class MyTest0(unittest.TestCase):
    def test_first_test(self):
        '''TC1 | test case description'''
        assert True
    def xtest_second_test(self):
        '''TC2 | test case description'''
        assert True
    def test_third_test(self):
        '''TC3 | test case description'''
        assert True

if __name__ == '__main__':
    nose.main(addplugins=[HtmlOutput()])
