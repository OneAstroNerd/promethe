from requests import get, post


response = post("https://promethe.vercel.app/")

print(response.text)