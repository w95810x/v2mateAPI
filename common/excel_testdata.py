# coding:utf-8
import xlrd
import xlutils
from xlutils.copy import copy

class Excel():
    '''excelPath= excel 的目录路径，sheetName = 自定义table'''

    # def __init__(self,excelPath,tableName='Sheet1'):
    #     self.workbook = xlrd.open_workbook(excelPath,formatting_info=True)
    #     self.sheet = self.workbook.sheet_by_name(tableName)
    #     self.keys = self.sheet.row_values(0)  # 获取第一行作为key值
    #     self.rowNum = self.sheet.nrows  # 获取总行数
    #     self.colNum = self.sheet.ncols  # 获取总列
    def get_workbook(self):
        work=xlrd.open_workbook(r"C:\Users\t-wangbingxuan-cj\Desktop\test.xls", formatting_info=True)
        return work

    def get_sheet(self):
        work = xlrd.open_workbook(r"C:\Users\t-wangbingxuan-cj\Desktop\test.xls", formatting_info=True)
        sheet = work.sheet_by_index(0)
        return sheet
    def get_rows(self):
        rows=self.get_sheet().nrows
        return rows

    def get_url(self,row,col):
        url = self.get_sheet().cell_value(row,col)
        return url

    def get_data(self,row,col):
        data = self.get_sheet().cell_value(row,col)
        return data

    def get_method(self,row,col):
        method = self.get_sheet().cell_value(row,col)
        return method

    def get_resuit(self,row,col):
        resuit = self.get_sheet().cell_value(row,col)
        return resuit
    def get_id(self,row,col):
        id = self.get_sheet().cell_value(row,col)
        return id






if __name__ == "__main__":
    data = Excel()
    res = data.get_url(1,2)
    print(res)

# import json
# import xlrd
# import requests
# import xlutils
# from xlutils.copy import copy
# workbook = xlrd.open_workbook(r"C:\Users\t-wangbingxuan-cj\Desktop\test.xls",formatting_info=True)
# sheet=workbook.sheet_by_index(0)
# workboowr=copy(workbook)
# wrsheetnwe=workboowr.get_sheet(0)
# wrsheet=workboowr.get_sheet(0)
#
# # wrsheet.write(1,10,excel_res)
# # workboowr.save((r"C:\Users\qa\Desktop\res-youtubetest.xls"))
#
# for i in range(1,sheet.nrows):
#     url = sheet.cell_value(i,2)
#     data = sheet.cell_value(i,5)
#     method = sheet.cell_value(i,3)
#     resuit = sheet.cell_value(i,8)
#     id=sheet.cell_value(i,0)
#     if method == 'post':
#         re = requests.post(url,data=data)
#         res = re.json()["msg"]
#         if res == resuit:
#             print((id), "-----》成功 ----》")
#             excel_res = "pass"
#         else:
#             print((id), "-----》失败 ----》")
#             excel_res = "fail"
#
#     elif method == 'get':
#         re = requests.get(url=url, data=data)
#         res = re.json()["msg"]
#         if res == resuit:
#             print((id), "-----》成功 ----》")
#             excel_res = "pass"
#         else:
#             print((id), "-----》失败 ----》")
#             excel_res = "fail"
#     wrsheetnwe.write(i,9,excel_res)
#     workboowr.save((r"C:\Users\t-wangbingxuan-cj\Desktop\test1.xls"))

