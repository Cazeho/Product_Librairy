
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import re
import json

#"https://www.carrefour.fr/r/boissons?noRedirect=1&page=1"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

url_list = []
for i in range(1,26):
  url_list.append('https://www.carrefour.fr/r/boissons?noRedirect=1&page=' + str(i))






#####################################
url="https://www.carrefour.fr/r/boissons?noRedirect=1&page=1"
result = requests.get(url)
obj = soup(result.content,'lxml')
data= obj.find_all('script', attrs={'type': 'text/javascript'})
html=data[4]




find= re.findall(r'window.ONECF_INITIAL_STATE = .*;', str(html))
k=find[0].replace("window.ONECF_INITIAL_STATE =","").replace(";","")

d=json.dumps(json.loads(k),sort_keys=True,indent=4)





with open("marques.json",'w') as file:
	file.write(json.dumps(json.loads(k),sort_keys=True,indent=4))

f=open("marques.json")
q=json.loads(f.read())



li=[]
for i in q["search"]["meta"]["facets"][1]["topTerms"]:
	print(i["label"])
	li.append(i["label"])

print(len(li))
