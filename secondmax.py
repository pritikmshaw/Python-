if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

z=max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print (max(arr))
# z=max(arr)
# print(z)
# newlist=arr.remove(z)
# print(arr)
# y=max(newlist)
# print (y)