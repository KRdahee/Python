import requests
from bs4 import BeautifulSoup
import csv

# 기본 URL 설정
base_url = "https://news.daum.net/foreign#1?page="

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
    
    # "오늘의 연재" 섹션 찾기
    today_series_section = soup.select('main > section > div:nth-of-type(1) > div:nth-of-type(5)')
    
    # 결과 추출
    for section in today_series_section:
        for article in section.find_all('a'):  # 가정: 각 연재는 <a> 태그 안에 있음
            title = article.get_text(strip=True)
            data.append([title])  # 링크 제외

# CSV 파일로 저장
csv_file = 'today_series.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 파일의 헤더 작성
    writer.writerow(['Title'])
    # 데이터 작성
    writer.writerows(data)

print(f'Data successfully saved to {csv_file}')
