T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    people = []
    for q in range(1, n + 1):
        people.append(q)

    for j in range(k):
        for p in range(1, n):
            people[p] += people[p - 1]
    print(people[-1])