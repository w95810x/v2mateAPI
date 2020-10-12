import json
import requests
import xlrd
import xlutils
from xlutils.copy import copy
import unittest
from common.excel_testdata import Excel
from common.request import testapi
from common.logs import logger
e=Excel()

rows=e.get_rows()
workbook=e.get_workbook()
book=copy(workbook)
sheet1=book.get_sheet(0)

class TestCase():
    def testcase(self):
        logger().info('----->开始执行-----》')
        for i in range(1,rows):
            url = e.get_url(i,2)
            data = e.get_data(i,5)
            method = e.get_method(i,3)
            resuit = e.get_resuit(i,8)
            id=e.get_id(i,0)
            re=testapi(method,url,data)
            resuit1=re.testApi()['msg']
            logger().info(resuit1)
            logger().info('--------------------------------------------------------------------------'
                          '-----------------------------------------')
            if resuit1 == resuit:
                print((id), "-----》成功 ----》")
                excel_res = "pass"
            else:
                print((id), "-----》失败 ----》")
                excel_res = "fail"
            sheet1.write(i,9,excel_res)
            sheet1.write(i,8,resuit1)
            book.save((r"C:\Users\t-wangbingxuan-cj\Desktop\test1.xls"))
        logger().info('----->执行完毕-----》')




            # if method == 'post':
            #     re = requests.post(url,data=data)
            #     res = re.json()["msg"]
            #     print(res)
            #     if res == resuit:
            #         print((id), "-----》成功 ----》")
            #         excel_res = "pass"
            #     else:
            #         print((id), "-----》失败 ----》")
            #         excel_res = "fail"
            #
            # elif method == 'get':
            #     re = requests.get(url=url, data=data)
            #     res = re.json()["msg"]
            #     print(res)
            #     if res == resuit:
            #         print((id), "-----》成功 ----》")
            #         excel_res = "pass"
            #     else:
            #         print((id), "-----》失败 ----》")
            #         excel_res = "fail"
            # sheet1.write(i,9,excel_res)
            # book.save((r"C:\Users\t-wangbingxuan-cj\Desktop\test1.xls"))


if __name__ == '__main__':
    a=TestCase()
    print(a.testcase())

