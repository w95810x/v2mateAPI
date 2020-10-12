import json
import requests

class testapi():
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    def testApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                if self.data == "":
                    print("No data post")
                else:
                    result = requests.post(self.url, data=self.data)
            elif self.method == 'get':
                if self.data == "":
                    result = requests.get(self.url)
                else:
                    result = requests.get(self.url, params=self.data)

            return result.json()
        except:
            print('失败')


