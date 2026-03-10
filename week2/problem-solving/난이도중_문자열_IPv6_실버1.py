# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

addr = input().strip()

idx_r2 = addr.find("::")
prev_num = 0

if idx_r2 == -1:
    pass
elif idx_r2 == 0:
    addr = addr.replace("::", "0000:")
else:
    addr = addr.replace("::", ":0000:")
    for i in range(idx_r2):
        if addr[i] == ":":
            prev_num += 1

unzip_sp = []
zip_sp = addr.split(":")

for word in zip_sp:
    if word == "":
        continue
    unzip_sp.append("0" * (4 - len(word)) + word)

while len(unzip_sp) < 8:
    unzip_sp.insert(prev_num + 1, "0000")

unzip = ":".join(unzip_sp)
print(unzip)


