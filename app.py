from requests import get, post


response = post("https://promethe.vercel.app?id=astro&passkey=astro1388")

print(response.text)