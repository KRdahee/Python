from bs4 import BeautifulSoup
import urllib.request

import pandas as pd

Hollys_stores = list() #여기에 할리스 매장 저장

for page in range(1, 51): #1 - 50
    
    Hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
    
    print(Hollys_url)
    
    html = urllib.request.urlopen(Hollys_url)
    
    soup_Hollys = BeautifulSoup(html, 'html.parser')
    
    tag_t_body = soup_Hollys.find('tbody') #tbody 테크를 찾아주세요.
    
    for store in tag_t_body.find_all('tr'):
        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address = store_td[3].string
        store_phone = store_td[5].string

        Hollys_stores.append([store_name] + [store_sido] + [store_address] + [store_phone])
        
        print(f'RESULT : \r\n{Hollys_stores}')
        
Hollys_tbl = pd.DataFrame(data=Hollys_stores, columns=('매장', '도시','주소','전화번호'))

Hollys_tbl.to_csv('./Hollys_table_EXCEL.csv', encoding= 'cp949', mode= 'w', index=True)

Hollys_tbl.to_csv('./Hollys_table.csv', encoding= 'utf-8', mode= 'w', index=True) #깨질것 생각해서.