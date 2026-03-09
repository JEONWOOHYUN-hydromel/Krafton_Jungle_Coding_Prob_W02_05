# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
input_str = input().upper()
score_dict = {}
for i in input_str:
    if i in score_dict:
        score_dict[i]+=1
    else:
        score_dict[i] = 1
most_ele = ("",0)
double_winner = False
for item in score_dict.items():
    if item[1] > most_ele[1]:
        most_ele = item
        double_winner = False
    elif item[1] == most_ele[1]:
        double_winner = True
if double_winner:
    print("?")
else:
    print(most_ele[0])
