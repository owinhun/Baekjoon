N = int(input())

g_w = 0

for i in range(N):
    word = input()
    n_word = 0
    
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            n_w = word[i+1:]
            if n_w.count(word[i]) > 0:
                n_word += 1

    if n_word == 0:
        g_w += 1
        
print(g_w)