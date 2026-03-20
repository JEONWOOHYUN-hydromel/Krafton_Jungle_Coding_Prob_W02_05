# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
import sys
input = sys.stdin.readline

n = int(input())

#dic 자리
nod = {}
for i in range(n):
    nod[i] = [0, 0, []]   # 0: 작업시간, 1: 진입차수, 2: 내가 가리키는 노드들

#n개의 잡 정보 가져오기, 겸 초기 실행 노드 추가
exe_nod = []
for i in range(n):
    info = list(map(int, input().split()))
    
    #작업 시간
    nod[i][0] = info[0]

    #선행 작업 수
    num_job = info[1]
    nod[i][1] = num_job
    if num_job == 0:
        exe_nod.append([i, info[0]])   # 0: idx, 1: 남은 작업 시간(정렬 기준)

    #선행 작업들의 리스트에 나 등록
    for j in range(num_job):
        nod[info[j+2]-1][2].append(i)   # 0 ~ n-1 번 노드

clock = 0
while exe_nod:
    endeds = []

    #남은 작업 시간으로 오름차순
    exe_nod.sort(key= lambda x: x[1])
    
    #빨리 끝나는거 빼기
    executed = exe_nod[0]
    endeds.append(executed[0])
    del exe_nod[0]

    #작업시간 적용
    clock += executed[1]

    #exe_nod에 시간 적용, 끝난 작업있는지 확인
    new_exe_nod = []
    for exe in exe_nod:
        exe[1] -= executed[1]
        if exe[1] == 0:
            endeds.append(exe[0])
        else:
            new_exe_nod.append(exe)
    exe_nod = new_exe_nod
    
    #끝난 선행 작업이 연결된 거 진입차수 갱신, 겸 진입차수 0인거 exe_nod에 추가
    for ended in endeds:
        for post in nod[ended][2]:
            nod[post][1] -= 1
            if nod[post][1] == 0:
                exe_nod.append([post, nod[post][0]])

print(clock)
    
