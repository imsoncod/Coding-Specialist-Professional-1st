# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(hour, minute):
    answer = ''
    hour_angle = float(hour) * 30.0 + float(minute) * 0.5
    min_angle = float(minute) * 6.0
    answer = abs(hour_angle - min_angle)

    return round(answer, 1)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 3
minute = 0
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")