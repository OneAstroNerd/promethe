from requests import get, post


response = post("https://promethe.vercel.app/gate?id=astro&passkey=astro1388")

print(response.text)