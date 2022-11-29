import requests
r = requests.get("https://www.computerhope.com/jargon/c/computer.htm")
print(r.text)