word = input().upper()
s_word = list(set(word))

cnt_li = []
for i in s_word:
    cnt = word.count(i)
    cnt_li.append(cnt)

if cnt_li.count(max(cnt_li)) > 1:
    print('?')
else:
    max_idx = cnt_li.index(max(cnt_li))
    print(s_word[max_idx])