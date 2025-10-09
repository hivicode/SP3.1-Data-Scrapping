#import library requests
import requests

result = requests.get("https://www.detik.com/")

print(result) #response
# print(result.text) #html

#response code
print(result.encoding)

#response url
print(result.url)

#response elapsed
print(result.elapsed)

#response status code
print(result.status_code)

#response headers
print(result.headers['Content-Type'])

#response history
print(result.history)