import requests
import re
from bs4 import BeautifulSoup
import json

user_input = input("Enter the material for the category you want: ")
url = "https://www.myntra.com/" + user_input+"?rawQuery="+user_input

print(url)

HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chsocrome/125.0.0.0 Safari/537.36','Accept-Language':'en-US , en;q=0.5'})

response = requests.get(url,headers=HEADERS)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
target_class= soup.find_all('div',class_="searchProduct")
print(target_class)

