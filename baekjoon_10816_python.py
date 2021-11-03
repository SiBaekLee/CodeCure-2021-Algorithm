from bisect import *

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = int(input())

to_find = list(map(int, input().split()))

for i in to_find:
    print(abs(bisect_left(arr, i) - bisect_right(arr, i)), end=' ')