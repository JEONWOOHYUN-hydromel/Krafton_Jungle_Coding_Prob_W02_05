# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def fib(n, mem = None):
    if n < 2:
        return n
    
    if mem is None:
        mem = {}
    
    if n in mem:
        return mem[n]

    newfib = fib(n-2, mem) + fib(n-1, mem)
    mem[n] = newfib
    return newfib

print(fib(int(input())))