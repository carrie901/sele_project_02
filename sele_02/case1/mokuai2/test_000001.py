# coding=utf-8
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    '''类加中文'''
    @classmethod
    def setUpClass(cls):
        print("所有用例之前只执行一次")
    @classmethod
    def tearDownClass(cls):
        print("所有用例之后只执行一次")
    def test_01(self):
        '''中文注释'''
        print("111111")
    def test_02(self):
        print("22222")
    def test_03(self):
        print("33333")
if __name__ =="__main__":
    unittest.main()