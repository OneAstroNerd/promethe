from requests import get


response = get("https://promethe.vercel.app/")

print(response.text)