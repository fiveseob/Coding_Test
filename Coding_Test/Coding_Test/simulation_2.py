def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              10: [3, 0], 0: [3, 1], 12: [3, 2]}

    left_key = [1, 4, 7]
    right_key = [3, 6, 9]

    left_f = 10  # 3,0
    right_f = 12  # 3,2
    now = 0

    for number in numbers:
        now = number
        if number in right_key:
            answer += 'R'
            right_f = now  # 그 위치로 이동
        elif number in left_key:
            answer += 'L'  # 출력하고
            left_f = now
        else:  # mid인 경우
            right_d = abs(now - right_f)
            left_d = abs(now - left_f)
            if right_d > left_d:  # right_d와 left_d 거리 비교해서 후처리
                answer += 'L'
                left_f = now
            elif right_d < left_d:
                answer += 'R'
                right_f = now
            elif right_d == left_d:
                if hand == 'left':
                    answer += 'L'
                    left_f = now
                else:
                    answer += 'R'
                    right_f = now

    return answer