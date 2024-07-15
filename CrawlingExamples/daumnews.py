
import requests
from bs4 import BeautifulSoup
import csv

# 기본 URL 설정
base_url = "https://news.daum.net/breakingnews/foreign?page="

# 데이터 저장을 위한 리스트 초기화
data = []

# 1페이지부터 10페이지까지 순회
for page in range(1, 11):
    # 각 페이지의 URL 설정
    url = f"{base_url}{page}"
    print(f"Scraping page {page}: {url}")
    
    # 웹페이지 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청에 실패하면 예외 발생
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 기사 정보 찾기
    articles = soup.select('ul.list_news2.list_allnews > li')
    
    # 결과 추출
    
    # articles 리스트의 각 기사(article)에 대해 반복문을 실행합니다.
for article in articles:
    # 기사의 제목을 포함하는 <strong> 태그 내의 <a> 태그를 선택합니다.
    title_tag = article.select_one('strong.tit_thumb > a.link_txt')
    # 기사의 출처를 포함하는 <span> 태그를 선택합니다.
    source_tag = article.select_one('span.info_news')
    # 기사의 시간을 포함하는 <span> 태그를 선택합니다.
    time_tag = article.select_one('span.info_time')
    
    # title_tag가 존재하면 텍스트를 가져오고, 없으면 "N/A"를 기본값으로 사용합니다.
    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    # source_tag가 존재하면 텍스트를 가져오고, 없으면 "N/A"를 기본값으로 사용합니다.
    source = source_tag.get_text(strip=True) if source_tag else "N/A"
    # time_tag가 존재하면 텍스트를 가져오고, 없으면 "N/A"를 기본값으로 사용합니다.
    time = time_tag.get_text(strip=True) if time_tag else "N/A"
    
    # title, source, time 정보를 data 리스트에 추가합니다.
    data.append([title, source, time])


# CSV 파일로 저장
csv_file = 'news_articles.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일의 헤더 작성
    writer.writerow(['Title', 'Source', 'Time'])
    # 데이터 작성
    writer.writerows(data)

print(f'Data successfully saved to {csv_file}')