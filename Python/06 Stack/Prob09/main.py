def solution(decimal):
    stack = []
    while(decimal > 0):
        tmp = (int) (decimal % 2) # 2로 나눈 나머지
        stack.append((str)(tmp)) # str로 변경
        decimal = (int) (decimal / 2) # 다음번 진행
    binary = "" # 2진수 표현
    while stack:
        binary += stack.pop() #join구문이 더 좋음

    print(binary)

    return binary

solution(15)
solution(13)
