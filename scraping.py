from bs4 import BeautifulSoup
import urllib.request
from collections import defaultdict

url='https://www.drugs.com/drug_information.html'

from urllib.request import Request, urlopen

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
url_f= urlopen(req).read()

soup=BeautifulSoup(url_f,'html.parser')

links={}
drugs={}
drugs=defaultdict(dict)

list1= soup.find_all('ul',{'class':'ddc-paging'})
#print(list1, end="\n ")

for i in list1:
    per_drugs=i.find_all('a')
#print(per_drugs, end=" \n")
for link in per_drugs:
    links[str(link.string)]=str(link.get('href'))
#print(links, end="\n")

#for x,y in links.items():
 #   print(const+y,x)

const='https://www.drugs.com'

def func(website,char):
    #print(char)
    req_1 = Request(website, headers={'User-Agent': 'Mozilla/5.0'})
    url_f_1= urlopen(req_1).read()
    soup_1=BeautifulSoup(url_f_1,'html.parser')

    list_1= soup_1.find_all('ul',{'class':'ddc-list-column-2'})
    
    for j in list_1:
        per_drugs_1=j.find_all('a')
    #print(per_drugs_1,end="\n")
    m=1
    for drug in per_drugs_1:
        
        drugs[str(char)][m]=str(drug.string)
        m=m+1
    
    

for x,y in links.items():
    func(const+y,x)

#print(drugs,end="\n")


q=input("enter letter ")

print(drugs[q])


    
