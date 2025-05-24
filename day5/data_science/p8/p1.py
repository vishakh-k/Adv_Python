import requests

#response=requests.get("https://api.github.com");

#print(response.text);

#print(response.json());

#print(response.status_code)


response=requests.delete("https://httpbin.org/delete");

print(response.json());

print(response.status_code)
