from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import csv  

Next_Daily = []  

for page in range(1, 100):  
    Daumforeign_url = f'https://news.daum.net/foreign#{page}' #국제뉴스 오늘의 연재
    
    html = urllib.request.urlopen(Daumforeign_url)  
    soup = BeautifulSoup(html, 'html.parser')  
    
    article_list = soup.select('body#timeline > ul.type1 li') 
    
    for article in article_list:
        time = article.find('em', class_='txt_time').text.strip()
        
        
        Next_Daily.append([real_time])

# 추출한 데이터로 DataFrame 생성
df = pd.DataFrame(Next_Daily, columns=['실시간'])

# CSV 파일로 저장
df.to_csv('./final_NextDaily_tabel_EXCEL.csv', encoding='utf-8', mode='w', index=False)

print(f'CSV 생성완료')