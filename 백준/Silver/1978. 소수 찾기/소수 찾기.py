num = int(input())
n = map(int, input().split())
ss = 0

for i in n:
  ev = 0
  if i > 1:
      for j in range(2, i):
          if  i % j == 0:
              ev += 1

      if ev == 0:
          ss += 1

print(ss)