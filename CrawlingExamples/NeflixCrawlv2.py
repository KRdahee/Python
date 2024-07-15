# Selenium 라이브러리를 임포트하여 웹 브라우저를 자동으로 조작
from selenium import webdriver

# Chrome WebDriver를 사용하여 웹 브라우저를 엽니다. 경로는 로컬에 저장된 chromedriver.exe 파일 위치입니다.
#이거 해야함 ㅋㅋ
browser = webdriver.Chrome('c:/??/chromedriver')

# 스크래핑할 URL을 설정합니다.
url = 'https://www.netflix.com/kr/browse/genre/839338'

# 지정한 URL로 웹 브라우저를 이동시킵니다.
browser.get(url)

# 현재 페이지의 소스 코드를 가져옵니다.
html = browser.page_source

# BeautifulSoup 라이브러리를 임포트하여 HTML을 파싱합니다.
from bs4 import BeautifulSoup

# 페이지 소스 코드를 BeautifulSoup 객체로 변환합니다.
soup = BeautifulSoup(html, 'html.parser')

# 'section' 태그를 모두 선택합니다.
section_list = soup.select('section')

# 결과를 저장할 빈 리스트를 만듭니다.
results = []

# 각 섹션을 순회합니다.
for section in section_list:
    # 섹션 내의 첫 번째 'h2' 태그의 텍스트를 섹션 제목으로 가져옵니다.
    section_title = section.select('h2')[0].text

    # 섹션 내의 모든 'li' 태그를 선택합니다.
    program_list = section.select('li')

    # 각 프로그램을 순회합니다.
    for program in program_list:
        # 프로그램 내의 첫 번째 'span' 태그의 텍스트를 프로그램 제목으로 가져옵니다.
        program_title = program.select('span.nm-collections-title-name')[0].text

        # 프로그램 내의 첫 번째 'img' 태그의 'src' 속성을 프로그램 이미지 URL로 가져옵니다.
        program_img = program.select('img')[0]['src']

        # 프로그램 내의 첫 번째 'a' 태그의 'href' 속성을 프로그램 링크로 가져옵니다.
        program_link = program.select('a')[0]['href']

        # 수집한 데이터를 리스트로 묶습니다.
        data = [section_title, program_title, program_img, program_link]

        # 결과 리스트에 데이터를 추가합니다.
        results.append(data)

# pandas 라이브러리를 임포트하여 DataFrame을 생성합니다.
import pandas as pd

# 수집한 데이터를 DataFrame으로 변환합니다.
df = pd.DataFrame(results)

# DataFrame의 컬럼명을 설정합니다.
df.columns = ['카테고리', '프로그램명', '이미지', '링크']

# DataFrame을 엑셀 파일로 저장합니다. 파일 경로와 이름을 지정합니다.
df.to_excel('c:/인프라수업자료/엑셀파일저장하기.xlsx')

#Netflix의 특정 장르 페이지를 스크래핑하여 각 섹션의 프로그램 정보를 추출하고, 이를 엑셀 파일로 저장하는 작업을 수행합니다. 
#주요 과정은 Selenium을 사용한 웹 페이지 로딩, BeautifulSoup을 사용한 HTML 파싱, pandas를 사용한 데이터 저장으로 구성됩니다.