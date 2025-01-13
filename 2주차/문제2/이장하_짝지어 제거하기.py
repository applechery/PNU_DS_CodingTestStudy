def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    if stack:
        return 0
    return 1


'''
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (9.15ms, 10.4MB)
테스트 3 〉	통과 (9.66ms, 10.4MB)
테스트 4 〉	통과 (9.03ms, 10.6MB)
테스트 5 〉	통과 (9.07ms, 10.6MB)
테스트 6 〉	통과 (9.58ms, 10.6MB)
테스트 7 〉	통과 (9.01ms, 10.7MB)
테스트 8 〉	통과 (10.06ms, 10.5MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 9.99MB)
테스트 16 〉	통과 (0.00ms, 9.96MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)

효율성 테스트
테스트 1 〉	통과 (84.06ms, 16.3MB)
테스트 2 〉	통과 (81.50ms, 11.8MB)
테스트 3 〉	통과 (84.31ms, 12.2MB)
테스트 4 〉	통과 (92.47ms, 12.3MB)
테스트 5 〉	통과 (90.25ms, 12.2MB)
테스트 6 〉	통과 (82.33ms, 12.2MB)
테스트 7 〉	통과 (84.25ms, 12.3MB)
테스트 8 〉	통과 (92.81ms, 14.7MB)
'''
