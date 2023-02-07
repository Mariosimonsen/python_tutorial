#1 System som heter requests    
#2 System som heter noe annet
import requests 
import httpx 

url = 'https://httpbin.org/get2'
'''data = {'key1': ['value1', 'value2']}
files = {'upload-file': ('mylicensefile.xls', open('LICENSE', 'rb'), 'application/ms.excel')}
myjson = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}'''

rr = requests.get(url)
print(rr.status_code)
if rr.status_code == 200:
    print('poggers')
else:
    print('sadge')
rr.raise_for_status()


hr = httpx.get(url)
print(hr.status_code)
 
if hr.status_code == httpx.codes.OK:
    print('poggers')
else:
    print('sadge')
