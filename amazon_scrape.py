import requests
import re
from bs4 import BeautifulSoup
import json

global_dict={}

def extract_fabric_percentages(text):
    regex = r"(?P<percentage>\d+(\.\d+)?)(?P<material>\s*%\s*\w+(?:,\s*\w+)*?)(?:\.|$)?"
    matches = re.finditer(regex, text)

    results = {}
    for match in matches:
        try:
            percentage = float(match.group('percentage'))  # Convert to float to handle decimals
            material = match.group('material').strip()
            results[material] = percentage
        except ValueError:
            print(f"Error: Unexpected format for percentage: {match.group('percentage')}")
    return results 
        



user_input = input("Enter the material for the category you want: ")
url = "https://www.amazon.in/s?k=" + user_input + "&ref=nb_sb_noss" 

print(url)

HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chsocrome/125.0.0.0 Safari/537.36','Accept-Language':'en-US , en;q=0.5'})

response = requests.get(url,headers=HEADERS)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
target_divs = soup.find_all('h2')
for divs in target_divs:
    anchor_tags=divs.find_all('a')
    for tag in anchor_tags:
        y=tag['href']
        url1="https://www.amazon.in/"+y
        print(url1)
        print()
        response1=requests.get(url1,headers=HEADERS)
        soup1 = BeautifulSoup(response1.content, 'html.parser')
        target_div = soup1.find('div',class_="a-fixed-left-grid-col a-col-right")
        if target_div:
           print(target_div.text)
           '''
           global_dict[url1]=extract_fabric_percentages(target_div.text)
           
data=global_dict


with open("data.json", "w") as outfile:
  json.dump(data, outfile, indent=4)  '''

            
        

        

  
