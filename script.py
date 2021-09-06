import requests

print("The version of the requests is: %s" % requests.__version__)

r = requests.get('http://www.google.com/')
print(r)