import httpx

url = ''

while True:
    movie = input('Enter the name of the movie your are looking for: ')
    if not movie:
        break