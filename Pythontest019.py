"""
물가 지수 조사하기
국내 한 지자체에서 물가 지수를 조사하기 위한 데이터입니다.

item : 조사한 품목명 리스트
last_month : 지난달 품목에 따른 금액 리스트
this_month : 이번달 품목에 따른 금액 리스트
물가 지수를 계산하는 방법은 다음과 같습니다.

((이번달 가격 / 지난달 가격) - 1)*100

반복문을 이용하여 각 물품의 물가 지수를 계산하고 출력해보는 프로그램을 만들어보겠습니다.

7번째 줄의 미션을 확인하고 len() 을 이용하여 변수 length 에 item의 리스트의 길이를 저장합니다.

11번째 줄의 미션을 확인하고 변수 length를 이용하여 반복문을 만들어보세요! (None은 지워주세요.)

14번째 줄의 미션을 확인하고 지난달 물가 데이터, 이번달 물가 데이터를 이용하여 물가 상승률을 계산합니다. (반드시 아래의 식만 이용해주세요.)

((이번달 물품 가격 / 지난달 물품 가격)-1) * 100

17번째 줄의 미션을 확인하고 다음과 같은 양식으로 출력합니다. (None은 지워주세요.)

설렁탕 : 7.394
치킨 : 15.9934

"""

for i in range(0, length):
    inflation_rate = (this_month[i] / last_month[i] - 1) * 100
    print(f'{item[i]}: {inflation_rate}')

    print('쓰레기봉투료', ":", '탕수육')

    ((이번달 가격 / 지난달 가격) - 1) * 100

# item 리스트의 길이를 저장합니다.
length = len(item)

# length 값을 이용하여 물가 상승률을 보여주는 반복문을 만들어 보세요!
for i in range(0, length):
    # 변수 inflation_rate에 물가 상승률을 계산해 보세요!
    inflation_rate = ((this_month[i] / last_month[i]) - 1) * 100
    # 품목명의 물가 상승률을 item 리스트의 순서대로 출력해 보세요!
    print(item[i] + ": " + str(inflation_rate))