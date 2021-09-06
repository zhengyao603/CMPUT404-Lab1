import requests

print("The version of the requests is: %s" % requests.__version__)

request1 = requests.get('http://www.google.com/')
request2 = requests.get('https://raw.githubusercontent.com/zhengyao603/CMPUT404-Lab1/main/script.py')

print(request1)
printt(request2.text)