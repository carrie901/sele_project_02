# coding=utf-8
import unittest
import time
from common.HTMLTestRunner_yo import HTMLTestRunner
# 找到case下所有用例 defaultTestLoader加载器（测试用例路径、匹配规则test开头，）
discover = unittest.defaultTestLoader.discover("D:\\sele_project_yutiantian\case1","test*.py")
print(discover)
                    #若测试用例在不同的路径下，可以将发现的用例合并在一个里面
                    # all = unittest.TestSuite()
                    # for i in discover:
                    #     all.addTests(i)
                    # for j in discover:
                    #     all.addTests(j)

# 时间戳  格式为年月日时分秒
nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")

# 测试报告保存地址。+及测试报告名称（加了时间戳）
reportpath = "D:\\sele_project_yutiantian\\report\\"+"report%s.html"%nowtime
# 写入权限
fp = open(reportpath,"wb")

runner=HTMLTestRunner(fp,
                      verbosity=2,
                      title="这是我的报告",#标题
                      description="报告内容如下",#内容
                      retry=1)  #失败重跑
# 运行测试用例
runner.run(discover)


#通过测试报告的失败或者成功是根据代言