# 문제 설명
# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

# 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
# 1 ≤ tangerine의 원소 ≤ 10,000,000
# 입출력 예
# k	tangerine	result
# 6	[1, 3, 2, 5, 4, 5, 2, 3]	3
# 4	[1, 3, 2, 5, 4, 5, 2, 3]	2
# 2	[1, 1, 1, 1, 2, 2, 2, 3]	1
# 입출력 예 설명
# 입출력 예 #1

# 본문에서 설명한 예시입니다.
# 입출력 예 #2

# 경화는 크기가 2인 귤 2개와 3인 귤 2개 또는 2인 귤 2개와 5인 귤 2개 또는 3인 귤 2개와 5인 귤 2개로 귤을 판매할 수 있습니다. 이때의 크기 종류는 2가지로 이 값이 최소가 됩니다.
# 입출력 예 #3

# 경화는 크기가 1인 귤 2개를 판매하거나 2인 귤 2개를 판매할 수 있습니다. 이때의 크기 종류는 1가지로, 이 값이 최소가 됩니다.

def solution(k, tangerine):
    dict = {}
    for tang in tangerine:
        if tang not in dict.keys():
            dict[tang] = 1
        else:
            dict[tang]+=1
    size_list = []
    for size in dict.keys():
        size_list.append(dict[size])
    size_list.sort()
    
    answer=0
    while(k>0):
        out = size_list.pop()
        k-=out
        answer+=1
    return answer

# 테스트 1 〉	통과 (35.69ms, 13.1MB)
# 테스트 2 〉	통과 (19.04ms, 13.2MB)
# 테스트 3 〉	통과 (17.81ms, 13.5MB)
# 테스트 4 〉	통과 (18.56ms, 13.1MB)
# 테스트 5 〉	통과 (14.37ms, 11.2MB)
# 테스트 6 〉	통과 (17.12ms, 11.5MB)
# 테스트 7 〉	통과 (17.22ms, 12.4MB)
# 테스트 8 〉	통과 (15.48ms, 11.9MB)
# 테스트 9 〉	통과 (19.80ms, 11.6MB)
# 테스트 10 〉	통과 (31.33ms, 12.9MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.16ms, 10.2MB)
# 테스트 22 〉	통과 (0.38ms, 10.4MB)
# 테스트 23 〉	통과 (0.24ms, 10.3MB)
# 테스트 24 〉	통과 (0.47ms, 10.2MB)
# 테스트 25 〉	통과 (5.84ms, 11.2MB)
# 테스트 26 〉	통과 (5.01ms, 11.7MB)
# 테스트 27 〉	통과 (62.67ms, 21.8MB)
# 테스트 28 〉	통과 (35.58ms, 16.2MB)
# 테스트 29 〉	통과 (33.18ms, 18.1MB)
# 테스트 30 〉	통과 (50.92ms, 22MB)
# 테스트 31 〉	통과 (17.08ms, 12.5MB)
# 테스트 32 〉	통과 (36.32ms, 13.7MB)
# 테스트 33 〉	통과 (31.95ms, 18.1MB)
# 테스트 34 〉	통과 (40.04ms, 18.1MB)

# 다른사람 풀이

import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer


# 테스트 1 〉	통과 (6.18ms, 13MB)
# 테스트 2 〉	통과 (5.78ms, 13.1MB)
# 테스트 3 〉	통과 (5.76ms, 13.5MB)
# 테스트 4 〉	통과 (6.81ms, 13.1MB)
# 테스트 5 〉	통과 (5.10ms, 11MB)
# 테스트 6 〉	통과 (5.11ms, 11.5MB)
# 테스트 7 〉	통과 (6.33ms, 12.7MB)
# 테스트 8 〉	통과 (6.05ms, 11.7MB)
# 테스트 9 〉	통과 (5.69ms, 11.6MB)
# 테스트 10 〉	통과 (12.82ms, 13MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.03ms, 10.3MB)
# 테스트 21 〉	통과 (0.06ms, 10.1MB)
# 테스트 22 〉	통과 (0.13ms, 10.1MB)
# 테스트 23 〉	통과 (0.26ms, 10.4MB)
# 테스트 24 〉	통과 (0.14ms, 10.3MB)
# 테스트 25 〉	통과 (1.65ms, 11.2MB)
# 테스트 26 〉	통과 (2.38ms, 11.7MB)
# 테스트 27 〉	통과 (22.38ms, 21.7MB)
# 테스트 28 〉	통과 (15.13ms, 16.2MB)
# 테스트 29 〉	통과 (17.76ms, 18.1MB)
# 테스트 30 〉	통과 (24.71ms, 21.7MB)
# 테스트 31 〉	통과 (6.76ms, 12.6MB)
# 테스트 32 〉	통과 (6.64ms, 13.6MB)
# 테스트 33 〉	통과 (24.24ms, 18.1MB)
# 테스트 34 〉	통과 (15.75ms, 17.9MB)


import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    lst = sorted(cnt.values())
    while(k>0):
        v = lst.pop()
        k-=v
        answer+=1
    return answer


# 테스트 1 〉	통과 (5.84ms, 13.2MB)
# 테스트 2 〉	통과 (6.00ms, 13.1MB)
# 테스트 3 〉	통과 (6.38ms, 13.4MB)
# 테스트 4 〉	통과 (6.84ms, 13.2MB)
# 테스트 5 〉	통과 (4.81ms, 11.2MB)
# 테스트 6 〉	통과 (5.94ms, 11.5MB)
# 테스트 7 〉	통과 (6.38ms, 12.7MB)
# 테스트 8 〉	통과 (9.12ms, 11.9MB)
# 테스트 9 〉	통과 (5.68ms, 11.6MB)
# 테스트 10 〉	통과 (6.90ms, 12.9MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)
# 테스트 17 〉	통과 (0.03ms, 10.1MB)
# 테스트 18 〉	통과 (0.02ms, 10.3MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.02ms, 10.1MB)
# 테스트 21 〉	통과 (0.10ms, 10.2MB)
# 테스트 22 〉	통과 (0.13ms, 10.3MB)
# 테스트 23 〉	통과 (0.17ms, 10.4MB)
# 테스트 24 〉	통과 (0.16ms, 10.4MB)
# 테스트 25 〉	통과 (2.77ms, 11.2MB)
# 테스트 26 〉	통과 (2.54ms, 11.7MB)
# 테스트 27 〉	통과 (24.60ms, 21.9MB)
# 테스트 28 〉	통과 (15.52ms, 16.2MB)
# 테스트 29 〉	통과 (24.27ms, 18.1MB)
# 테스트 30 〉	통과 (44.27ms, 21.8MB)
# 테스트 31 〉	통과 (7.89ms, 12.6MB)
# 테스트 32 〉	통과 (11.90ms, 13.6MB)
# 테스트 33 〉	통과 (17.48ms, 18MB)
# 테스트 34 〉	통과 (17.04ms, 18.1MB)