# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
n = int(input())
arr = [input().strip() for _ in range(n)]

# arr = ["had", "adsfa", "poiop"]

dic = {}
for word in arr:

    if word == word[::-1]:
        print(len(word), word[len(word)//2])
        break

    if word not in dic:
        dic[word[::-1]] = word[len(word)//2]
    else:
        print(len(word), dic[word])
        break