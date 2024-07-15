import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_10_thrillers_korean_netflix():
    # Netflix 한국 페이지의 미국 스릴러 영화 URL / 라이브러리 임포트: requests 라이브러리를 사용하여 HTTP 요청을 보내고 BeautifulSoup을 사용하여 HTML을 파싱합니다.
    url = 'https://flixpatrol.com/top10/netflix/world/today/full/#netflix-2'  # Crime Thrillers 코드

    # GET 요청을 URL로 보냄. GET 요청 보내기: 해당 URL로 GET 요청을 보내고 요청이 성공했는지 확인합니다.
    response = requests.get(url)
    if response.status_code != 200:
        print('웹페이지를 불러오는데 실패했습니다.')
        return []

    #웹페이지 파싱: BeautifulSoup을 사용하여 HTML 내용을 파싱합니다.
    soup = BeautifulSoup(response.content, 'html.parser')

    # 상위 10개 영화가 포함된 섹션을 찾습니다
    # 이 예제에서는 특정 HTML 구조를 찾아야 합니다
    top_10_section = soup.find_all('div', class_='lolomoRow lolomoRow_title_card ltr-0')  # 올바른 클래스나 ID로 변경

    top_10_movies = []
    for movie in top_10_section[:10]:  # 상위 10개가 섹션의 첫 10개 항목이라고 가정
        title_tag = movie.find('aria-label')  # 예: 제목이 포함된 실제 HTML 태그로 'h3'를 변경
        if title_tag:
            title = title_tag.text
            top_10_movies.append(title)

    return top_10_movies

if __name__ == "__main__":
    top_10_thrillers = get_top_10_thrillers_korean_netflix()
    if top_10_thrillers:
        print("Netflix 한국에서 상위 10개의 미국 스릴러 영화:")
        for idx, movie in enumerate(top_10_thrillers, start=1):
            print(f"{idx}. {movie}")

        # CSV 파일로 저장
        df = pd.DataFrame(top_10_thrillers, columns=['Title'])
        df.to_csv('./top_10_thrillersEXCEL.csv', encoding='cp949', mode='w', index=True)
        df.to_csv('./top_10_thrillers.csv', encoding='utf-8', mode='w', index=True)
        #엑셀 파일은 cp949 인코딩을 사용하고, 일반적인 목적의 CSV 파일은 utf-8 인코딩을 사용합니다
    else:
        print("상위 10개의 스릴러 영화를 가져오는데 실패했습니다.")


#참고:
#HTML 구조: 실제 Netflix 사이트의 HTML 구조는 자주 변경될 수 있으므로, Netflix 페이지를 검사하여 정확한 선택자를 찾아야 합니다.
#동적 콘텐츠: Netflix는 종종 JavaScript를 사용하여 콘텐츠를 동적으로 로드하므로, 초기 HTML 응답에 콘텐츠가 포함되어 있지 않으면 Selenium과 같은 도구를 사용해야 할 수도 있습니다.
#페이지 검사:
#Netflix 페이지를 검사하고 올바른 선택자를 찾으려면 웹 브라우저의 개발자 도구를 사용하세요 (페이지에서 마우스 오른쪽 버튼을 클릭하고 "검사" 또는 "요소 검사"를 선택). 
#영화 제목이 포함된 태그와 클래스를 찾아 BeautifulSoup 선택자를 적절히 조정하세요.
#예제 URL: Netflix의 한국 사이트에서 미국 스릴러 영화에 해당하는 실제 URL과 선택자로 스크립트의 URL과 선택자를 변경해야 합니다.
#HTML 태그 수정: title_tag를 찾은 후 그 텍스트를 가져오기 전에 확인합니다.
#실패 시 빈 리스트 반환: 요청이 실패하면 빈 리스트를 반환하여 이후 오류를 방지합니다.
#CSV로 저장: 영화 목록을 DataFrame으로 변환하고 CSV로 저장합니다.
#실제 영화 제목이 포함된 HTML 요소의 클래스 이름이나 다른 식별 속성으로 변경해야 합니다.
