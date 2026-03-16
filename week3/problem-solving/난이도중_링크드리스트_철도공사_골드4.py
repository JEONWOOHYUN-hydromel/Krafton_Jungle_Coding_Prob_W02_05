# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stations = list(map(int, input().split()))

class Node:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

station_dict = {}

# 첫 노드 생성
head = Node(stations[0])
station_dict[stations[0]] = head
prev_node = head

# 나머지 노드 연결
for i in range(1, n):
    new_node = Node(stations[i])
    station_dict[stations[i]] = new_node

    prev_node.next = new_node
    new_node.prev = prev_node
    prev_node = new_node

# 원형 연결
tail = prev_node
head.prev = tail
tail.next = head

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "BN":
        i = int(cmd[1])
        j = int(cmd[2])

        #print
        target = station_dict[i]
        next_st = target.next
        print(next_st.num)

        #add
        new_node = Node(j)
        station_dict[j] = new_node

        target.next = new_node
        new_node.prev = target
        new_node.next = next_st
        next_st.prev = new_node

    elif cmd[0] == "BP":
        i = int(cmd[1])
        j = int(cmd[2])

        #print
        target = station_dict[i]
        prev_st = target.prev
        print(prev_st.num)

        #add
        new_node = Node(j)
        station_dict[j] = new_node

        prev_st.next = new_node
        new_node.prev = prev_st
        new_node.next = target
        target.prev = new_node

    elif cmd[0] == "CN":
        i = int(cmd[1])

        #print
        target = station_dict[i]
        delete_node = target.next
        print(delete_node.num)

        #delete
        next_next = delete_node.next
        target.next = next_next
        next_next.prev = target

        del station_dict[delete_node.num]

    elif cmd[0] == "CP":
        i = int(cmd[1])

        #print
        target = station_dict[i]
        delete_node = target.prev
        print(delete_node.num)

        #delete
        prev_prev = delete_node.prev
        prev_prev.next = target
        target.prev = prev_prev

        del station_dict[delete_node.num]