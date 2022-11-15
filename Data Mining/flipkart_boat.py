import requests
import pandas as pd
from bs4 import BeautifulSoup
def get(url):
    page= requests.get(url)
    if page.status_code==200:
        return BeautifulSoup(page.text,'lxml')
    else:
        print('Error:',page.status_code)
        return None


def extract(soup):
    target = soup.find('div', class_='_1YokD2 _3Mn1Gg')
    products = target.find_all('div',class_='_1AtVbE col-12-12')
    print("products:",len(products))
    info= []
    for item in products:
        name=item.find('div',class_='_4rR01T')
        s_price=item.find('div',class_='_30jeq3 _1_WHN1')
        o_price=item.find('div',class_='3I9_wc _27UcVY')
        rating=item.find('div',class_='_3LWZlK')
        rating_count=item.find('span',class_='gUuXy-')
        data = {}
        try:
            data['name'] = name.text.strip()
        except:
            data['name']=None
        try:
            data['s_price'] = s_price.text.strip()
        except:
            data['s_price']=None
        try:
            data['o_price'] = o_price.text.strip()
        except:
            data['o_price']=None
        try:
            data['rating'] = rating.text.strip()
        except:
            data['rating']=None
        try:
            data['rating_count'] = rating_count.text.strip()
        except:
            data['rating_count']=None
        info.append(data)
        print('Extracted:',name)
    return info

def save(data_list):
    if len(data_list) > 0:
        pd.DataFrame(data_list).to_csv('flipkart.csv',index=False)
    else:
        print('No data To save')



def main():
    pos=1
    product = 'television'
    datalist =[]
    while True:

        url = 'https://www.flipkart.com/search?q=television&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        soup = get(url)
        if not soup:
            break
        data = extract(soup)
        if data:
            datalist.extend(data)
            pos +=1
        else:
            break
    save(datalist)

main()