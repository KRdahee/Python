"""

야구에서 타자의 성적을 보는 지표는 다양합니다. 그 중에서 타율이 제일 대표적인 지표입니다.

그리고 이를 계산하기 위한 지표는 다음과 같습니다.

타석수 : 타자가 공을 치기 위해 들어선 모든 기회의 수
안타수 : 타자가 공을 친 결과, 안타(1루타, 2루타, 3루타, 홈런)의 개수
예를 들면, 타자 A가 100번의 타석에서 37개의 안타를 치면 타율은 0.370(0.37)이라고 합니다.

타석수와 1루타부터 홈런까지의 각각의 개수를 가진 리스트를 넣으면 타율을 계산하는 batting_average 함수를 만들어보겠습니다.


타석수와 안타수를 입력하면 타율을 계산하는 함수 batting_average()를 작성해봅시다.

인자 : 리스트 score (순서 : 타석수(1이상의 자연수), 1루타 개수, 2루타 개수, 3루타 개수, 홈런 개수)
반환값 : 타율(소수점 셋째 자리까지)
단, 안타(홈런포함)의 개수가 타석수보다 많으면 -1 을 반환하세요.


"""
#예시1

# 타석수 : 1000, 1루타 : 100, 2루타 : 23, 3루타 : 10, 홈런 : 0 (총 안타 : 133)
batting_score = [1000, 100, 23, 10, 0]
print(batting_average(batting_score))
# 0.133

#예시2 

# 타석수 : 100, 1루타 : 100, 2루타 : 23, 3루타 : 10, 홈런 : 0 (총 안타 : 133)
# 타석수보다 안타수가 더 많으므로 -1 반환
batting_score = [100, 100, 23, 10, 0]
print(batting_average(batting_score))
# -1

"""
Hints!
일반적으로 타율은 소수점 셋째 자리까지 표시됩니다. 예를 들면 타율 계산 결과가 0.30866425992779783이라면 0.3086…에서 6을 반올림한 0.387이 됩니다.

파이썬에서는 반올림하는 함수 round()가 있습니다. 숫자와 표시할 소수점자리를 입력하면 반올림하여 계산해줍니다.

"""

#예시1

avg = 0.30866425992779783

# avg의 소수점 3번째 자리까지 보겠다.
avg = round(avg, 3)

print(avg)
# 0.387

#예시2

avg = 0.3300000

# avg의 소수점 3번째 자리가 0이면 소수점 2번째 자리까지 보여집니다.
avg = round(avg, 3)

print(avg)
# 0.33

# 정답


# 타석과 안타 정보가 담긴 리스트가 인자로 주어지면 조건을 만족하도록
# 타율을 계산하는 함수 batting_average()를 작성해봅시다.
def batting_average(batting_score):
    total_at_bats = batting_score[0]
    total_hits = sum(batting_score[1:])
    
    if total_hits > total_at_bats:
        return -1
    
    average = total_hits / total_at_bats
    average = round(average, 3)
    
    return average

batting_score = [1000, 100, 23, 10, 0]
print(batting_average(batting_score))

batting_score = [100, 100, 23, 10, 0]
print(batting_average(batting_score))

score = [7132, 1197, 464, 28, 467]
print(batting_average(score))
# 이승엽 선수의 한국 야구 통산 타석수, 1루타 개수, 2루타 개수, 3루타 개수, 홈런 개수
