def get_prevalue(driver): #이름, 세부정보 url, 이미지url 가져오기
    #시리즈주소 입력
    driver.get(serise_url_up)
    #리스트 생성
    S_name=[]
    S_url=[]
    S_img=[]
    #pgdown 반복
    for i in range(0, 400, 1): #page_down 할 횟수
        driver.find_element(by='tag name', value='body').send_keys(Keys.PAGE_DOWN) # 페이지다운 반복
        time.sleep(0.1)
        
    slider_items = driver.find_elements(by='xpath',value='//div[starts-with(@class, "slider-item")]')

    for item in slider_items:
        tag = item.find_element(by='xpath', value='.//a')
        name = anchor_tag.get_attribute('aria-label')
        url = anchor_tag.get_attribute('href')
        image_url = item.find_element(by='xpath', value='.//img').get_attribute('src')

        S_name.append(name)
        S_url.append(url)
        S_img.append(image_url)
        
    S_detail = [url.split('?')[0].replace("/watch/", "/browse/genre/83?so=az&jbv=") for url in S_url]    
    return S_name, S_url, S_img, S_detail

def get_detailvalue(driver, S_name, S_detail):  #세부정보 가져오기 크리에이터, 출연, 장르, 시리즈특징, 관람등급, 방송사, 상영일자
    S_creator = []  # 크리에이터
    S_actor = []  # 출연
    S_genre = []  # 장르
    S_char = []  # 시리즈 특징
    S_age = []  # 관람 등급
    S_BC = []  # 방송사
    S_year = []  # 상영일자

    for detail_url in S_detail:
        driver.get(detail_url)

        # 클래스 요소 찾기
        tags = driver.find_elements(by='class name', value='previewModal--tags')

        # 기본값 설정
        creator = None
        actor = None
        genre = None
        char = None
        BC = None
        age = None
        year = None

        for tag in tags:
            label = tag.find_element(by='class name', value='previewModal--tags-label').text
            items = tag.find_elements(by='class name', value='tag-item')

            if label == '출연:':
                actor = [item.text for item in items]
            elif label == '크리에이터:':
                creator = [item.text for item in items]
            elif label == '장르:':
                genre = [item.text for item in items]
            elif label == '시리즈 특징:':
                char = [item.text for item in items]

        # 관람등급 가져오기
        try:
            maturity_wrapper = driver.find_element(by='class name', value='maturity-rating-wrapper')
            BC = maturity_wrapper.find_element(by='class name', value='maturity-number').text
            age = maturity_wrapper.find_element(by='class name', value='maturityDescription').text
        except NoSuchElementException:
            BC = None
            age = None

        # 방송사 가져오기
        try:
            broadcaster_element = driver.find_element(by='class name', value='broadcaster')
            BC = broadcaster_element.find_element(by='tag name', value='div').text
            year = broadcaster_element.find_element(by='tag name', value='div').text
        except NoSuchElementException:
            BC = None
            year = None

        # 정보를 리스트에 저장
        S_creator.append(creator if creator else None)
        S_actor.append(actor if actor else None)
        S_genre.append(genre if genre else None)
        S_char.append(char if char else None)
        S_BC.append(BC if BC else None)
        S_age.append(age if age else None)
        S_year.append(year if year else None)
        
    return S_creator, S_actor, S_genre, S_char, S_BC, S_age, S_year