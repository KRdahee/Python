"""
Bello, Tulaliloo ti amo!
영화 <슈퍼 배드>에 나오는 미니언즈는 Minionese라고 하는 신기한 언어를 사용합니다.
우리가 미니언 용어를 모르기 때문에 Minionese를 한국어로 번역해주는 사전을 하나 만들고자 합니다.

아래 미니언 용어 사전을 참고해서
key = Minionese, value = 한국어인 Dictionary를 변수 miniWord에 담아봅시다. 

"""

cvs = ["Bello", "Bello", "Tulaliloo_ti_amo", "Tank_yu", "Poopaye", "Poopaye"]

#위 대응관계 (Minionese→한국어)를 가진 Dictionary - miniWord를 만들어봅시다.

miniWord = {'Bello':'안녕','Poopaye':'잘가','Tank_yu':'고마워','Tulaliloo_ti_amo':'우린 너를 사랑해'}

#변수 cvs에 미니언들이 한 말들이 리스트에 담겨 있습니다. miniWord를 이용해 이를 한국어로 한 줄에 하나씩 번역해봅시다.

for x in cvs:
    print(miniWord[x])

