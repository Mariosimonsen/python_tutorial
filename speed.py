import httpx
import re
import time
import asyncio

def count_https_in_web_pages():
    with open('topsites.txt') as file:
        urls = [line.strip() for line in file.readlines()]
    
    htmls = [httpx.get(url).text for url in urls]
   
    count_https = 0
    count_http = 0

    for html in htmls:
        count_https += len(re.findall('https://', html))
        count_http += len(re.findall('http://', html))
    
    print('This is result')
    time.sleep(1)
    print(count_https)
    print(count_http)
    print(count_https/count_http)


#count_https_in_web_pages()

async def better_count_https_in_web_pages():
    with open('topsites.txt') as file:
        urls = [line.strip() for line in file.readlines()]
    
    #htmls = [httpx.get(url).text for url in urls]
    async with httpx.AsyncClient() as client:
        task = (client.get(url, follow_redirects=True)for url in urls)
        reqs = await asyncio.gather(*task)

    htmls = [req.text for req in reqs]


    count_https = 0
    count_http = 0

    for html in htmls:
        count_https += len(re.findall('https://', html))
        count_http += len(re.findall('http://', html))
    
    print('This is result')
    print(count_https)
    print(count_http)
    print(count_https/count_http)

asyncio.run(better_count_https_in_web_pages())